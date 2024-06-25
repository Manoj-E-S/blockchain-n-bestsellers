# make a middleware wrapper function that decodes a jwt token and adds the user to the request object
from flask import request
from ..Utils.jwt import decode

def auth_middleware(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token:
            try:
                decodedToken = decode(token)
                request.user = decodedToken["user"]
                return func(*args, **kwargs)
            except Exception as e:
                return {"error": str(e)}, 401
        else:
            return {"error": "No token provided"}, 401
    return wrapper