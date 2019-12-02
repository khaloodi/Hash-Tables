import time
import hashlib
import bcrypt

key = b"hello"

print(hashlib.sha256(key).hexdigest())