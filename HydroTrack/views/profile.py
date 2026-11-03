import streamlit as st

from services import (
    get_goal,
    set_goal
)


def show(user):

    user_id = user["id"]

    st.title("👤 Profile")

    st.subheader("Account Information")

    st.write(
        f"**Username:** {user['username']}"
    )

    st.divider()

    st.subheader("Hydration Goal")

    current_goal = get_goal(user_id)

    default_goal = 0

    if current_goal:
        default_goal = current_goal[0]["daily_goal_ml"]

    goal = st.number_input(
        "Daily Goal (mL)",
        min_value=0,
        value=default_goal,
        step=100
    )

    if st.button("Save Goal"):

        set_goal(
            user_id,
            goal
        )

        st.success(
            "Hydration goal updated successfully!"
        )

        st.rerun()