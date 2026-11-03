import streamlit as st
from datetime import datetime, timedelta

from services import (
    add_water_log,
    get_water_logs,
    edit_water_log,
    delete_water_log
)


def show(user):

    user_id = user["id"]

    st.title("💧 Water Log")

    st.subheader("Add Water Intake")

    amount = st.number_input(
        "Amount (mL)",
        min_value=0,
        step=100
    )

    if st.button("Add Water Intake"):

        add_water_log(
            user_id,
            amount
        )

        st.success(
            f"{amount} mL added successfully!"
        )

        st.rerun()

    st.divider()

    st.subheader("Water Intake History")

    logs = get_water_logs(user_id)

    if not logs:

        st.info(
            "No water intake records available."
        )

        return

    for log in logs:

        with st.container():

            col1, col2, col3 = st.columns(
                [3, 2, 1]
            )

            with col1:

                utc_time = datetime.fromisoformat(
                    log["logged_at"]
                )

                ph_time = utc_time + timedelta(hours=8)

                formatted_date = ph_time.strftime(
                    "%b %d, %Y %I:%M %p"
                )

                st.write(
                    f"📅 {formatted_date}"
                )

            with col2:

                new_amount = st.number_input(
                    "Amount",
                    min_value=0,
                    value=log["amount_ml"],
                    key=f"edit_{log['id']}"
                )

            with col3:

                if st.button(
                    "Save",
                    key=f"save_{log['id']}"
                ):

                    edit_water_log(
                        log["id"],
                        new_amount
                    )

                    st.success(
                        "Entry updated."
                    )

                    st.rerun()

                if st.button(
                    "Delete",
                    key=f"delete_{log['id']}"
                ):

                    delete_water_log(
                        log["id"]
                    )

                    st.success(
                        "Entry deleted."
                    )

                    st.rerun()

            st.divider()