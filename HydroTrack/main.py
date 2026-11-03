import streamlit as st
from services import register_user, login_user

st.set_page_config(
    page_title="HydroTrack",
    page_icon="💧",
    layout="wide"
)

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# If not logged in, show Login/Register
if not st.session_state.logged_in:

    st.title("💧 HydroTrack")
    st.subheader("Smart Hydration Management System")

    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )

    # LOGIN TAB
    with login_tab:

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login"):

            user = login_user(
                username,
                password
            )

            if user:
                st.session_state.logged_in = True
                st.session_state.user = user[0]

                st.success("Login successful!")

                st.rerun()

            else:
                st.error("Invalid username or password")

    # REGISTER TAB
    with register_tab:

        new_username = st.text_input(
            "Username",
            key="register_username"
        )

        new_password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )

        if st.button("Register"):

            try:

                register_user(
                    new_username,
                    new_password
                )

                st.success(
                    "Account created successfully!"
                )

            except Exception as e:

                st.error(
                    f"Registration failed: {e}"
                )

# Logged in
else:

    st.success(
        f"Welcome, {st.session_state.user['username']}!"
    )

    st.write(
        "Dashboard coming soon..."
    )

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user = None

        st.rerun()