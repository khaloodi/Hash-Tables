import time
import hashlib
import bcrypt

key = b"hello"

print(hashlib.sha256(key).hexdigest())


def djb2(key):
    # start from an arbitrarily large prime number
    hash_value = 5381

    # bit-shift and sum value for each character

    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char