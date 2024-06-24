import base64
import json

def get_name_and_email(oauth_credentials):
    idToken = oauth_credentials._id_token
    stringBytes = base64.b64decode(idToken.split(".")[1])
    string = stringBytes.decode('utf-8')
    jsonObj = json.loads(string)
    email = jsonObj['email']
    name = jsonObj['name']
    return name, email