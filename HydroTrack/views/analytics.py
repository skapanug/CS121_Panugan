import streamlit as st
import pandas as pd
import plotly.express as px

from services import get_water_logs


def show(user):

    st.title("📊 Analytics")

    user_id = user["id"]

    logs = get_water_logs(user_id)

    if not logs:

        st.info(
            "No water intake data available."
        )

        return

    df = pd.DataFrame(logs)

 
    
    total_intake = df["amount_ml"].sum()

    average_intake = round(
        df["amount_ml"].mean(),
        2
    )

    total_entries = len(df)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💧 Total Intake",
            f"{total_intake} mL"
        )

    with col2:
        st.metric(
            "📊 Average Intake",
            f"{average_intake} mL"
        )

    with col3:
        st.metric(
            "📝 Total Entries",
            total_entries
        )

    st.divider()


    # Daily Intake Chart
    st.subheader(
        "Daily Intake Records"
    )

    chart1 = px.bar(
        df,
        x="logged_at",
        y="amount_ml",
        labels={
            "logged_at": "Date",
            "amount_ml": "Water Intake (mL)"
        }
    )

    st.plotly_chart(
        chart1,
        use_container_width=True
    )

    st.divider()

  
    # Trend Chart
    st.subheader(
        "Hydration Trend"
    )

    chart2 = px.line(
        df,
        x="logged_at",
        y="amount_ml",
        markers=True,
        labels={
            "logged_at": "Date",
            "amount_ml": "Water Intake (mL)"
        }
    )

    st.plotly_chart(
        chart2,
        use_container_width=True
    )
