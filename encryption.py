"""
Module for encrypting and decrypting data with a master password (and providing
necessary information for decryption such as salt and initialization vector)
"""

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util import Counter
from Crypto import Random


KEY_BYTES = 32
SALT_BYTES = 8


def encrypt(password: str, plaintext: str) -> tuple[bytes, bytes, bytes]:
    """
    Encrypt the provided plaintext with the provided password returning the
    initialization vector, salt, and ciphertext.
    """
    # choose a random 16-byte initialization vector and a random 8 bit salt
    iv = Random.new().read(AES.block_size)
    salt = Random.new().read(SALT_BYTES)

    # convert the initialization vector to an integer
    iv_int = int.from_bytes(iv, 'big')

    # create a key with the password and salt
    key = PBKDF2(password, salt, KEY_BYTES)

    # create a counter for use by the AES cipher with the integer
    # initialization vector
    counter = Counter.new(AES.block_size * 8, initial_value=iv_int)

    # create the AES-CTR cipher
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)

    # encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))

    # return the initialization vector, salt, and ciphertext as they are
    # all needed for decryption
    return (iv, salt, ciphertext)


def decrypt(password: str, iv: bytes, salt: bytes, ciphertext: bytes) -> str:
    """
    Decrypt the provided ciphertext into plaintext with the provided password,
    initialization vector, and salt
    """
    assert len(iv) == 16

    # convert the initialization vector to an int
    iv_int = int.from_bytes(iv, 'big')

    # create the key with the password and salt
    key = PBKDF2(password, salt, KEY_BYTES)

    # initialize counter for use by the AES cipher
    counter = Counter.new(AES.block_size * 8, initial_value=iv_int)

    # create the AES-CTR cipher
    aes = AES.new(key, AES.MODE_CTR, counter=counter)

    # decrypt the ciphertext
    plaintext = aes.decrypt(ciphertext).decode('utf-8')

    return plaintext

