from db import supabase
from models import User, HydrationGoal, WaterLog
import hashlib

def register_user(username, password):
    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    result = supabase.table("users").insert({
        "username": username,
        "password_hash": password_hash
    }).execute()

    return result

def login_user(username, password):
    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    result = (
        supabase.table("users")
        .select("*")
        .eq("username", username)
        .eq("password_hash", password_hash)
        .execute()
    )

    return result.data




def set_goal(user_id, daily_goal_ml):
    existing_goal = (
        supabase.table("hydration_goals")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    if existing_goal.data:
        return (
            supabase.table("hydration_goals")
            .update({
                "daily_goal_ml": daily_goal_ml
            })
            .eq("user_id", user_id)
            .execute()
        )

    return (
        supabase.table("hydration_goals")
        .insert({
            "user_id": user_id,
            "daily_goal_ml": daily_goal_ml
        })
        .execute()
    )


def get_goal(user_id):
    result = (
        supabase.table("hydration_goals")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    return result.data


def add_water_log(user_id, amount_ml):
    return (
        supabase.table("water_logs")
        .insert({
            "user_id": user_id,
            "amount_ml": amount_ml
        })
        .execute()
    )

def get_water_logs(user_id):
    result = (
        supabase.table("water_logs")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    return result.data

def calculate_progress(total_intake, goal):
    if goal == 0:
        return 0

    return round(
        (total_intake / goal) * 100,
        2
    )

def get_hydration_status(total_intake, goal):
    if total_intake >= goal:
        return "Hydrated"

    elif total_intake >= goal * 0.75:
        return "Nearly Achieved"

    elif total_intake >= goal * 0.50:
        return "Moderately Hydrated"

    return "Needs More Water"

def get_recommendation(total_intake, goal):
    remaining = goal - total_intake

    if total_intake >= goal:
        return "Great job! You reached your hydration goal."

    return f"Drink {remaining} mL more water to reach your goal."


def edit_water_log(log_id, new_amount_ml):
    return (
        supabase.table("water_logs")
        .update({
            "amount_ml": new_amount_ml
        })
        .eq("id", log_id)
        .execute()
    )

def delete_water_log(log_id):
    return (
        supabase.table("water_logs")
        .delete()
        .eq("id", log_id)
        .execute()
    )


