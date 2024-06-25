import base64
import json

def get_user_credentials(oauth_credentials):
    token = oauth_credentials.token
    refresh_token = oauth_credentials._refresh_token
    idToken = oauth_credentials._id_token
    stringBytes = base64.b64decode(idToken.split(".")[1])
    string = stringBytes.decode('utf-8')
    jsonObj = json.loads(string)
    email = jsonObj['email']
    name = jsonObj['name']
    return token, refresh_token, name, email