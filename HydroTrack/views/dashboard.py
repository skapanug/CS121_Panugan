import streamlit as st


def show():

    st.title("🏠 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Daily Goal",
            "0 mL"
        )

    with col2:
        st.metric(
            "💧 Current Intake",
            "0 mL"
        )

    with col3:
        st.metric(
            "🚰 Remaining",
            "0 mL"
        )

    st.divider()

    st.subheader("Hydration Progress")

    st.progress(0)

    st.write("0% Complete")

    st.divider()

    st.subheader("Hydration Status")

    st.info(
        "Please set a hydration goal."
    )

    st.divider()

    st.subheader("Recommendation")

    st.write(
        "Set your hydration goal in the Profile page to begin tracking your progress."
    )