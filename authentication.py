import streamlit as st
from streamlit_oauth import OAuth2Component
import os

def authorize():
    # Only show authentification if not already authorized
    if not authorized():
        auth_method = os.environ.get('AUTH_METHOD')
        if auth_method == 'oauth':
            authorize_oauth()
        elif auth_method == 'password':
            authorize_password()

def authorized():
    auth_method = os.environ.get('AUTH_METHOD')

    # Authentification needed?
    if auth_method is None or auth_method == "" or auth_method == "none":
        # st.info("No authentication method specified. Set the AUTH_METHOD environment variable to 'oauth' or 'password'.")
        return True
    
    if auth_method == 'oauth':
        return 'token' in st.session_state
    elif auth_method == 'password':
        return st.session_state.get("password_validated", False)

def authorize_oauth():
    AUTHORIZE_URL = os.environ.get('AUTHORIZE_URL')
    TOKEN_URL = os.environ.get('TOKEN_URL')
    REFRESH_TOKEN_URL = os.environ.get('REFRESH_TOKEN_URL')
    REVOKE_TOKEN_URL = os.environ.get('REVOKE_TOKEN_URL')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
    SCOPE = os.environ.get('SCOPE')

    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_URL, TOKEN_URL, REFRESH_TOKEN_URL, REVOKE_TOKEN_URL)

    # Check if token exists in session state
    # if 'token' not in st.session_state:
    result = oauth2.authorize_button("Login", REDIRECT_URI, SCOPE)
    if result and 'token' in result:
        # If authorization successful, save token in session state
        st.session_state.token = result.get('token')
        st.rerun()
    # else:
        # token = st.session_state['token']
        # st.json(token)
        # if st.button("Refresh Token"):
            # If refresh token button is clicked, refresh the token
            # token = oauth2.refresh_token(token)
            # st.session_state.token = token
            # st.rerun()    

def authorize_password():
    # if not st.session_state.get("password_validated", False):
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )

def password_entered():
    if st.session_state["password"] == os.environ["PASSWORD"]:
        st.session_state["password_validated"] = True
        del st.session_state["password"]  # Don't store the password.
    else:
        st.error("😕 Password incorrect")
        st.session_state["password_validated"] = False