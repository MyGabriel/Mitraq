# File: mitraq_classes

"""Importing classes and functions from other Mitraq files"""
from analysis import tracking
import mitraqdb
from mitraqdb import User, Habit

# This function, 'dashboard()', provides dashboard for logged-in users. It invokes functions
# like 'habit_menu()', 'tracking()', and 'delete_habit()'
# Note: Take note of the 'user' argument."""
def dashboard(user):
    while True:
        print(f"\n{"_"*10}| {user.name.upper()}'S MITRAQ |{"_"*10}\nDASHBOARD\n1. Profile\n2. Habit\n3. "
              f"Tracking\n4. Delete\n5. Exit")
        choice = input("Select: ")
        if choice == '1':
            print(f"\n{"_"*10}| {user.name.upper()}'S MITRAQ |{"_"*10}\nUSER'S INFORMATION\n"
                  f"Name: {user.name}\nAge: {user.age}\nCountry: {user.country}\nID: {user.user_id}")
        elif choice == '2':
            habit_menu(user)
        elif choice == '3':
            tracking(user)
        elif choice == '4':
            print(f"\n{"_" * 10}| {user.name.upper()}'S MITRAQ |{"_" * 10}")
            mitraqdb.delete_habit(user.user_id)
        elif choice == '5':
            print("Exited successfully.")
            break

# This is the 'habit_menu()' function. It initiates 'Habits' class and calls functions like
# 'add_habits()' from class 'User' and 'save_habits()'
# Note: It gives the 'user' five(5) pre-defined habits and a 6th option for
# habit customization.
def habit_menu(user):
    """The five(5) pre-defined habits dictionary."""
    habits = ["Quit Smoking", "Quit Alcoholism", "Meditate", "Go To Gym", "Reading"]
    print(f"\n{"_"*10}| {user.name.upper()}'S MITRAQ |{"_"*10}"
          f"\nChoose from the list of habits below.\nOr create your habit to track using 6."
          f"\nHABITS MENU")

    # for' function to iterate over the habits."""
    for idx, h in enumerate(habits, 1):
        print(f"{idx}. {h}")
    print(f"6. Create Custom Habit")
    choice = int(input("Choose: "))
    if choice in range(1, 6):
        name = habits[choice-1]
    else:
        name = input(f"\n{"_"*10}| {user.name.upper()}'S MITRAQ |{"_"*10}\nEnter habit name: ")

    # This code block helps user to set up date and time to track chosen habit.
    freq = 'daily' if input(f"\n{"_"*10}| {user.name.upper()}'S MITRAQ |{"_"*10}\n"
                            f"Frequency (1 for Daily, 2 for Weekly): ") == '1' else 'weekly'
    start_date = input(f"Start date (YYYY-MM-DD): ")
    start_time = input("Start time (HH:MM): ")

    habit = Habit(name, freq, start_date, start_time)
    user.add_habit(habit)
    mitraqdb.save_habit(user.user_id, habit)





# IU-International University of Applied Sciences
# Course Code: DLBDSOOFPP01
# Author: Gabriel Manu
# Matriculation ID: 9212512