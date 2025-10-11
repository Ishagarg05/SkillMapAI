import streamlit as st
import pyrebase
from dotenv import load_dotenv
import os

def app():
    load_dotenv()

    # Firebase Config
    firebaseConfig = {
        "apiKey": "AIzaSyCr3im9zKcCqnOObUkbFokNWay1s77BfNY",
        "authDomain": "ai-powered-roadmap.firebaseapp.com",
        "projectId": "ai-powered-roadmap",
        "storageBucket": "ai-powered-roadmap.appspot.com",
        "messagingSenderId": "488070928735",
        "appId": "1:488070928735:web:xxxxxxx",
        "databaseURL": "https://ai-powered-roadmap-default-rtdb.firebaseio.com/"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    st.title("👤 Account - Login / SignUp")

    menu = ["Login", "SignUp"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "SignUp":
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")

        if st.button("Sign Up"):
            if len(password) < 6:
                st.warning("Password must be at least 6 characters.")
            else:
                try:
                    auth.create_user_with_email_and_password(email, password)
                    st.success("✅ Account created! Please login.")
                except Exception as e:
                    st.error(e)

    elif choice == "Login":
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state["user_email"] = email
                st.session_state["logged_in"] = True  # ✅ Save login state
                st.success(f"✅ Logged in as {email}")
            except Exception as e:
                st.error(e)

    # ✅ Logout button (visible only if logged in)
    # if st.session_state.get("logged_in"):
    #     if st.button("Logout"):
    #         st.session_state["logged_in"] = False
    #         st.session_state.pop("user_email", None)
    #         st.warning("🚪 Logged out successfully")
    # ✅ Logout button (visible only if logged in)
        if st.session_state.get("logged_in"):
            if st.button("Logout"):
                st.session_state.clear()  # sab hata do
                st.warning("🚪 Logged out successfully")

