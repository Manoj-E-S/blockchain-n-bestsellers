from flask import session, request, url_for
import google.oauth2.credentials
import google_auth_oauthlib.flow


def get_auth_url(path_to_client_secret: str, redirect_uri: str, scopes: list[str]):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            path_to_client_secret, 
            scopes
        )

    flow.redirect_uri = redirect_uri
    authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            login_hint='hint@example.com',
            prompt='consent'
        )
    return authorization_url, state


def get_credentials(path_to_client_secret: str, scopes: list[str]):
    state = session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        path_to_client_secret,
        scopes,
        state=state)
    print(url_for('auth.dashboard', _external=True))
    flow.redirect_uri = url_for('auth.dashboard', _external=True)
    print(flow.redirect_uri)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)
    return flow.credentials