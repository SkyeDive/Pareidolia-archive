"""
Module for writing/reading encrypted data to/from images
"""
from PIL import Image
import logging

def __insert_byte(pixel: tuple[int,int,int,int], byte: int) -> tuple[int, int, int, int]:
    """
    Weave 1 byte into 1 pixel, leaving significant bits unchanged
    """
    new_r = pixel[0] & 252 | (byte & 3)
    new_g = pixel[1] & 252 | ((byte & (3 << 2)) >> 2)
    new_b = pixel[2] & 252 | ((byte & (3 << 4)) >> 4)
    new_a = pixel[3] & 252 | ((byte & (3 << 6)) >> 6)
    return (new_r,new_g,new_b,new_a)


def add_transparency(img_path: str) -> bool:
    try:
        with Image.open(img_path) as img:
            if img.format != "PNG" or img.mode != "RGB":
                return False
            else:
                img.putalpha(255)
                img.save(img_path)
                return True

    except Exception as e:
        logging.exception(f"An exception occurred while trying to add transparency: {e}")
        return False


def check_image_path(img_path: str, loading_vault = True, needs_png = True) -> bool:
    """
    Check the validity of the image path
    loading_vault: use image reading context for validity - require alpha channel/png format, check length bytes
    needs_png: require png format check - can be false if making a new vault and checking the source image's path,
               as write_to_image can convert source file to png when saving to a new destination
    """
    h_size = 29

    try:
        with Image.open(img_path) as img:
            if img.format != "PNG" and (loading_vault or needs_png):
                #print("failed png check")
                return False

            if img.mode != "RGBA" and (img.mode != "RGB" or loading_vault):
                #print("failed RGBA check")
                return False

            if img.width * img.height < h_size:
                #print("failed h_size")
                return False

            if loading_vault:
                len_byte = [0,0,0,0]
                for i in range(1,5):
                    len_byte[i-1] = __extract_byte(img.getpixel(((h_size-i)%img.width,(h_size-i)//img.height)))[0]

                cipher_length = len_byte[3] << 24 | len_byte[2] << 16 | len_byte[1] << 8 | len_byte[0]
                if img.width * img.height < h_size + cipher_length:
                    #print("failed to upload large enough image")
                    return False

            return True

    except Exception as e:
        return False


def write_to_image(img_path: str, enc_data: bytes, new_img_path = None) -> None:
    """
    Write the provided data into the least significant bits of the given image
    If new_img_path is not specified, will save in-place
    """
    #header: 25 bytes fixed length data, 4 bytes ciphertext length
    h_size = 29

    with Image.open(img_path) as img:
        #if the source isn't png, and if we're not saving to a new png file
        if img.format != "PNG" and (new_img_path is None or new_img_path.lower()[-3:] != "png"):
            raise Exception(f"invalid image format: expected PNG, got {img.format}")

        if img.mode != "RGB" and img.mode != "RGBA":
            raise Exception(f"invalid image mode: expected RGB/RGBA, got {img.mode}")

        #add alpha channel if not present
        if not img.has_transparency_data:
            img.putalpha(255)

        if len(enc_data) < h_size:
            raise Exception("malformed data header")

        img_data = img.getdata()
        if len(img_data) < len(enc_data):
            raise Exception(f"image too small: at least {len(enc_data):,} square pixels expected, got {len(img_data):,}");

        #get image's current pixels, loop until the bytes end
        img_pixels = list(img_data)
        data_ind = 0
        for pixel_ind in range(len(img_pixels)):
            if data_ind >= len(enc_data):
                break

            #replace least significant bits of current pixel with data of current byte
            img_pixels[pixel_ind] = __insert_byte(img_pixels[pixel_ind], enc_data[data_ind])
            data_ind += 1

        #push pixel changes and save
        img.putdata(img_pixels)
        if new_img_path is None:
            img.save(img_path)
        else:
            img.save(new_img_path)


def __extract_byte(pixel: tuple[int,int,int,int]) -> bytes:
    """
    Pull least significant bits from a pixel and reformat into a byte
    """
    cur_byte = ((pixel[3] & 3) << 6) | ((pixel[2] & 3) << 4) | ((pixel[1] & 3) << 2) | (pixel[0] & 3)
    return cur_byte.to_bytes(length=1, byteorder='big')


def pull_from_image(img_path: str) -> bytes:
    """
    Extract the encrypted data from the provided image and return as bytes
    """
    h_size = 29

    with Image.open(img_path) as img:
        if img.format != "PNG":
            raise Exception(f"invalid image format: expected PNG, got {img.format}")

        if img.mode != "RGBA":
            raise Exception(f"invalid image mode: expected RGBA, got {img.mode}")

        img_data = img.getdata()
        if len(img_data) < h_size:
            raise Exception("invalid image data: size too small")

        #read header data for conditions and returning
        img_header = b""
        for i in range(h_size):
            img_header += __extract_byte(img_data[i])

        cipher_length = img_header[h_size-4] << 24 | img_header[h_size-3] << 16 | img_header[h_size-2] << 8 | img_header[h_size-1]
        if len(img_data) < h_size + cipher_length or cipher_length <= 0:
            raise Exception("invalid image data: incorrect data length")

        #read ciphertext and return
        ciphertext = b""
        for i in range(h_size, h_size+cipher_length):
            ciphertext += __extract_byte(img_data[i])

        return img_header + ciphertext
