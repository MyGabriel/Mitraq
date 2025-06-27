# File: analysis

"""Importing classes and functions from other Mitraq files"""
import mitraqdb
from mitraqdb import User, Habit

"""This function, 'tracking()', assist users to monitor and analyse 'user' data"""
def tracking(user):
    print(f"\n{"_"*10}| {user.name.upper()}'S MITRAQ |{"_"*10}\nMITRAQ TRACKING\n"
          f"1. In Progress\n2. Completed\n3. Analysis")
    option = input("Choose: ")
    if option == '1':
        print(f"\n{"_" * 10}| {user.name.upper()}'S MITRAQ |{"_" * 10}")
        for h in user.habits:
            """Providing 30 prompts and linking it the 30 space from 'records' variable
               the '__init__()' function of the 'Habits' class."""
            for i in range(30):
                if h.records[i] is None:
                    """Receiving a mark for habits completion; yes (y) or no (n)."""
                    complete = input(f"Mark {h.name} ({h.frequency}) Day {i+1} complete? (y/n): ").lower()
                    """Assigning a mark to the spaces in 'records' variable"""
                    h.records[i] = (complete == 'y')
                    mitraqdb.save_habit(user.user_id, h)
                    break

    elif option == '2':
        print(f"\n{"_" * 10}| {user.name.upper()}'S MITRAQ |{"_" * 10}"
              f"\nBelow is your progress, {user.name}")
        """Iterating 'habits' data to display weather 'user' marked 'y' (✔), 'n' (✘)
           or has not responded (_), if the 'user' chooses option 2."""
        for h in user.habits:
            record_display = [
                '✔' if r else '✘' if r is False else '_' for r in h.records
            ]
            print(f"{h.name.upper()} → {' '.join(record_display)}")
    elif option == '3':
        print(f"\n{"_" * 10}| {user.name.upper()}'S MITRAQ |{"_" * 10}\nANALYSIS")
        """This code block iterate 'habits' data for analysis; revealing the 'longest'
           and 'shortest' streaks, if the 'user' chooses option 3."""
        for h in user.habits:
            longest, shortest = h.get_streaks()
            print(f"{h.name.upper()} — Longest streak: {longest}, Shortest streak: {shortest}")





# IU-International University of Applied Sciences
# Course Code: DLBDSOOFPP01
# Author: Gabriel Manu
# Matriculation ID: 9212512