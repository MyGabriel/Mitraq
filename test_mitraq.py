# File: test_mitraq

"""Importing Python libraries, classes and functions from other Mitraq files"""
from mitraq_classes import dashboard
from mitraqdb import save_habit, Habit, User
from datetime import datetime

# Manually defining the user to registration and login)
user = User("Gabriel", 99, "Ghana", "TYU6IP")

# Defining 14-day tracking records (True = ✔, False = ✘)
records_quit = [True, False, True, True, False, True, True, True, False, True, True, True, False, True]
records_meditate = [True, True, False, True, True, True, False, False, True, True, True, True, True, False]

# Creating two habits and assigning them records
habit1 = Habit("Quit Smoking", "daily", "2025-06-01", "06:00")
habit1.records[:14] = records_quit

habit2 = Habit("Meditate", "weekly", "2025-06-01", "21:00")
habit2.records[:14] = records_meditate

# Adding habits to user
user.add_habit(habit1)
user.add_habit(habit2)

# Saving habits to database
save_habit(user.user_id, habit1)
save_habit(user.user_id, habit2)

# Launching the dashboard
dashboard(user)




# IU-International University of Applied Sciences
# Course Code: DLBDSOOFPP01
# Author: Gabriel Manu
# Matriculation ID: 9212512