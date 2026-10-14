"""
Module for packing and unpacking ciphertext and related information (salt,
initialization vector) into a series of bytes
"""

import struct

VERSION = 1

V1_FORMAT = '> b 8s 16s L'
#            | |  |  |  \-> 32 bit unsigned integer for ciphertext length
#            | |  |  \-> 16 bytes for initialization vector
#            | |  \-> 8 bytes for password salt
#            | \-> 8 bit unsigned integer for version number
#            |
#            \-> big endian format

def pack_data(init_vector: bytes, salt: bytes, ciphertext: bytes) -> bytes:
    """
    Pack data (16 bit AES initialization vector, 8 byte password salt,
    arbitrary length ciphertext) into a series of bytes
    """
    if len(init_vector) != 16:
        raise Exception(f'expected 16 byte AES initialization vector, got {len(init_vector)} bytes')

    if len(salt) != 8:
        raise Exception(f'expected 8 bytes salt, got {len(salt)} bytes')

    if len(ciphertext) > (2**32 - 1):  # max value of 32 bit length field
        raise Exception('ciphertext too long to be stored')

    out = struct.pack(V1_FORMAT, 1, salt, init_vector, len(ciphertext))
    out += ciphertext

    return out

def unpack_data(data: bytes) -> tuple[bytes, bytes, bytes]:
    """
    Unpack data from series of bytes into 16 byte AES initialization vector, 8
    byte password salt, and arbitrary length ciphertext
    """
    _, salt, init_vector, cipher_length = struct.unpack_from(V1_FORMAT, data)
    
    offset = struct.calcsize(V1_FORMAT)  # index of start of ciphertext
    ciphertext = data[offset : offset+cipher_length]

    return init_vector, salt, ciphertext

