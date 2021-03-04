import binascii
import sys

from passlib.crypto import digest as pl_digest
from passlib.utils import random as pl_random

if len(sys.argv) < 3:
    print("Usage: {} username password".format(sys.argv[0]))
    sys.exit(1)


username = sys.argv[1]
password = sys.argv[2]

rounds = 8000
salt = pl_random.randbytes(8)
generated_hash = pl_digest.pbkdf2_hmac("sha384", password, salt, rounds)

print(
    """Username: {}
Password: {}
Hash:     {}
Salt:     {}
Rounds:   {}""".format(
        username,
        password,
        binascii.hexlify(generated_hash).decode(),
        binascii.hexlify(salt).decode(),
        rounds,
    )
)
