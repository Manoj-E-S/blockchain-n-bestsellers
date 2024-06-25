import jwt
from ..app_setup import get_jwt_secret
from datetime import datetime, timedelta

_jwt_secret = get_jwt_secret()

def encode(data):
    # set expiration of token in 2 hours
    payload = {"user": data,  "exp": datetime.utcnow() + timedelta(hours=2)}
    encoded_jwt = jwt.encode(payload, _jwt_secret, algorithm='HS256')
    return encoded_jwt

def decode(token):
    decoded_jwt = jwt.decode(token, _jwt_secret, algorithms=['HS256'])
    return decoded_jwt