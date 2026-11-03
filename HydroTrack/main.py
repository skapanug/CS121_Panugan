import streamlit as st
from views.profile import show as show_profile
from views.dashboard import show as show_dashboard
from views.water_log import show as show_water_log
from services import register_user, login_user

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="HydroTrack",
    page_icon="💧",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# =========================
# PLACEHOLDER PAGES
# =========================






def show_analytics():
    st.title("📊 Analytics")
    st.write("Analytics coming soon...")





# =========================
# LOGIN / REGISTER
# =========================

if not st.session_state.logged_in:

    st.title("💧 HydroTrack")
    st.subheader("Smart Hydration Management System")

    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )

    # -------------------------
    # LOGIN
    # -------------------------

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

                st.rerun()

            else:
                st.error(
                    "Invalid username or password."
                )

    # -------------------------
    # REGISTER
    # -------------------------

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

# =========================
# LOGGED IN AREA
# =========================

else:

    with st.sidebar:

        st.title("💧 HydroTrack")

        page = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Water Log",
                "Analytics",
                "Profile"
            ]
        )

        st.divider()

        if st.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.user = None

            st.rerun()

    if page == "Dashboard":
        show_dashboard(
        st.session_state.user
    )

    elif page == "Water Log":
        show_water_log(
        st.session_state.user
    )


    elif page == "Analytics":
        show_analytics()

    elif page == "Profile":
        show_profile(
        st.session_state.user
    )