import time
import hashlib
import bcrypt

key = b"hello"

sha256key = hashlib.sha256(key).hexdigest()

# print(sha256key)


def djb2(key):
    # start from an arbitrarily large prime number
    hash_value = 5381

    # bit-shift and sum value for each character

    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value

# print(djb2(key))

djb2key = djb2(key) 

# print(f"sha256 key: {int(sha256key) % 10}")
print(f"djb2key: {djb2key % 10}")
