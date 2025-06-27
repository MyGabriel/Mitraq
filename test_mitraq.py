from datetime import datetime

# Import your core components
from mitraq_classes import dashboard
from mitraqdb import save_habit, Habit, User

# Manually define the user (skip login/registration)
user = User("Gabriel", 99, "Ghana", "TYU6IP")

# Define 14-day tracking records (True = ✔, False = ✘, None = _)
records_quit = [True, False, True, True, False, None, True, True, False, True, True, True, False, None]
records_meditate = [True, None, False, None, True, None, None, False, True, True, None, None, True, None]

# Create two habits and assign records
habit1 = Habit("Quit Smoking", "daily", "2025-06-01", "06:00")
habit1.records[:14] = records_quit

habit2 = Habit("Meditate", "weekly", "2025-06-01", "21:00")
habit2.records[:14] = records_meditate

# Add habits to user
user.add_habit(habit1)
user.add_habit(habit2)

# Save habits to database
save_habit(user.user_id, habit1)
save_habit(user.user_id, habit2)

# Launch the dashboard
dashboard(user)