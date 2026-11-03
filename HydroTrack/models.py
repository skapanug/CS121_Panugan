class User:
    def __init__(self, username, password_hash, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash


class HydrationGoal:
    def __init__(self, user_id, daily_goal_ml, goal_id=None):
        self.goal_id = goal_id
        self.user_id = user_id
        self.daily_goal_ml = daily_goal_ml


class WaterLog:
    def __init__(self, user_id, amount_ml, logged_at=None, log_id=None):
        self.log_id = log_id
        self.user_id = user_id
        self.amount_ml = amount_ml
        self.logged_at = logged_at