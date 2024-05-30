from passlib.hash import sha256_crypt

def hash_password(password):
    return sha256_crypt.hash(password)

def verify_password(password, hash):
    return sha256_crypt.verify(password, hash)