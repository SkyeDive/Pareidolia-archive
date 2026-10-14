from enum import Enum, auto

import json
from encryption import decrypt, encrypt
from packing import pack_data, unpack_data
from password_entry import PasswordEntry
from data_entry import DataEntry
from steganography import check_image_path, pull_from_image, write_to_image


class VaultType(Enum):
    PASSWORD = auto()
    DATA = auto()

class DecryptionError(Exception):
    pass

class ImageReadingError(Exception):
    pass

class ImageWritingError(Exception):
    pass

class UnpackingError(Exception):
    pass

class DecodingError(Exception):
    pass

class EncodingError(Exception):
    pass

class DeserializationError(Exception):
    pass

def get_vault_entries(filepath: str, master_password: str) -> tuple[list[DataEntry | PasswordEntry], VaultType | None]:
    """
    Get the contents of the vault located at the filepath indicated using the
    master password.

    Returns a list of the entries (DataEntry or PasswordEntry) and the type of
    the entries from the VaultType Enum or None if no entries were located in
    the vault.

    May throw an ImageReadingError, DecodingError, or DecryptionError.
    """

    try:
        # get the raw data out of the image:
        if not check_image_path(filepath):
            raise ImageReadingError(f"Failed to read the contents of '{filepath}'")

        try:
            raw_image_data = pull_from_image(filepath)
        except Exception as e:
            raise ImageReadingError(f"Failed to read the contents of '{filepath}'") from e

        # unpack the information necessary for decryption from the raw data:
        try:
            initialization_vector, salt, ciphertext = unpack_data(raw_image_data)
        except Exception as e:
            raise DecodingError(f"Failed to unpack data from '{filepath}'")

        # decrypt the ciphertext:
        try:
            plaintext = decrypt(
                master_password,
                initialization_vector,
                salt,
                ciphertext
            )
        except Exception as e:
            raise DecryptionError(f"Failed to decrypt the contents of '{filepath}'") from e

        # deserialize the JSON entries to python objects:
        json_entries = json.loads(plaintext)

        if not isinstance(json_entries, list):
            raise DecodingError(f"Encrypted contents of JSON are not a valid list of entries")

        if len(json_entries) == 0:
            return [], None

        data_entries = []
        vault_type = VaultType.PASSWORD if 'password' in json_entries[0] else VaultType.DATA

        try:
            if vault_type == VaultType.PASSWORD:
                for entry in json_entries:
                    data_entries.append(PasswordEntry(**entry))
            elif vault_type == VaultType.DATA:
                for entry in json_entries:
                    data_entries.append(DataEntry(**entry))
        except json.JSONDecodeError:
            raise DecodingError('Error encountered while decoding JSON image contents')

        return data_entries, vault_type
    except:
        return None

def save_vault_entries(entries: list[DataEntry] | list[PasswordEntry], filepath: str, master_password: str):
    """
    Save the provided entries (DataEntry or PasswordEntry) to the filepath
    provided with the provided master password.

    May throw an EncodingError, ImageReadingError, or ImageWritingError.
    """

    # sending data to serialized form:
    try:
        json_contents = '[' + ','.join(e.to_json() for e in entries) + ']'
    except Exception as e:
        raise EncodingError('Failed to serialize entries to JSON') from e

    # encrypting:
    intialization_vector, salt, ciphertext = encrypt(
        master_password,
        json_contents
    )

    # packing data:
    try:
        raw_data = pack_data(intialization_vector, salt, ciphertext)
    except Exception as e:
        raise EncodingError('Failed to encode entries')

    if not check_image_path(filepath, loading_vault=False, needs_png=False):
        raise ImageReadingError(f"Filepath '{filepath}' is invalid")

    try:
        write_to_image(filepath, raw_data)
    except Exception as e:
        raise ImageWritingError(f"Failed to write to image '{filepath}'\nError message: {e}") from e

