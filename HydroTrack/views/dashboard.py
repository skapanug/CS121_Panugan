import streamlit as st

from services import (
    get_goal,
    get_water_logs,
    calculate_progress,
    get_hydration_status,
    get_recommendation
)


def show(user):

    user_id = user["id"]

    goal_data = get_goal(user_id)

    if not goal_data:

        st.title("🏠 Dashboard")

        st.warning("No hydration goal set. Please set a hydration goal in your Profile page.")

        return

    goal = goal_data[0]["daily_goal_ml"]

    logs = get_water_logs(user_id)

    total_intake = sum(
        log["amount_ml"]
        for log in logs
    )

    remaining = max(
        goal - total_intake,
        0
    )

    progress = calculate_progress(
        total_intake,
        goal
    )

    status = get_hydration_status(
        total_intake,
        goal
    )

    recommendation = get_recommendation(
        total_intake,
        goal
    )

    st.title("🏠 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Daily Goal",
            f"{goal} mL"
        )

    with col2:
        st.metric(
            "💧 Current Intake",
            f"{total_intake} mL"
        )

    with col3:
        st.metric(
            "🚰 Remaining",
            f"{remaining} mL"
        )

    st.divider()

    st.subheader("Hydration Progress")

    st.progress(progress / 100)

    st.write(
        f"{progress}% Complete"
    )

    st.divider()

    st.subheader("Hydration Status")

    st.info(
        status
    )

    st.divider()

    st.subheader("Recommendation")

    st.write(
        recommendation
    )