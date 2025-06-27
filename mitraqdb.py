#File: mitraqdb

"""Importing build-in Python libraries."""
import sqlite3
import secrets
import string

"""Connecting mitraq.db to sqlite3 for data storage and processing"""
conn = sqlite3.connect('mitraqdata.db')
c = conn.cursor()

"""
The next 3 code blocks build 2 tables in sqlite3.
   Note: The first table, 'users', stores user's information (name, age, country, and user_id).
   The second table, habits, stores history including date and time,
   and the third commits data in the tables.
"""
c.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT, age INTEGER, country TEXT, user_id TEXT PRIMARY KEY)""")

c.execute("""CREATE TABLE IF NOT EXISTS habits (
    user_id TEXT, habit_name TEXT, frequency TEXT, start_date TEXT, start_time TEXT, records TEXT)""")

conn.commit()

"""This function, 'generate_user_id()', generates a unique code for users with
'string' and 'secret' Python libraries."""
def generate_user_id():
    token = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(token) for _ in range(6))

"""This function, 'register()', gets user's information for registration. It calls
'generate_user_id()' function and commit the 'users' table, """
def register():
    print("\nREGISTRATION")
    name = input("Name: ").capitalize()
    age = int(input("Age: "))
    country = input("Country: ").capitalize()
    user_id = generate_user_id()
    """Connecting 'users' table to store user's information."""
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (name, age, country, user_id))
    conn.commit()
    print(f"Your User ID is {user_id}, save it for login.")
    return user_id

"""This function, 'login()', it fetches 'user_id' from 'users' table, calls 'User' class,
'load_habits()' function.
   Note: The 'user' arguments from 'dashboard()' is assigned to 'User' class's data"""
def login():
    print("\nLOGIN\nUse your User ID to login.")
    user_id = input("Enter User ID: ")
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    data = c.fetchone()
    if data:
        user = User(*data)
        user.habits = load_habits(user_id)
        return user
    else:
        print("User not found.")
        return None

"""This function, 'save_habit()', connects and update the 'habits' table."""
def save_habit(user_id, habit):
    records = ','.join(['1' if r else '0' if r is False else 'N' for r in habit.records])
    c.execute("REPLACE INTO habits VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, habit.name, habit.frequency, habit.start_date, habit.start_time, records))
    conn.commit()

"""This function, 'load_habits()', connects and loads users habits history using user_id."""
def load_habits(user_id):
    # Fetching habits data with user_id from the 'habits' table
    c.execute("SELECT * FROM habits WHERE user_id=?", (user_id,))
    rows = c.fetchall()
    habits = []
    for row in rows:
        # Linking the 'Habit' class (particularly, 'records' variable) to append stored data.
        h = Habit(row[1], row[2], row[3], row[4])
        h.records = [True if r == '1' else False if r == '0' else None for r in row[5].split(',')]
        habits.append(h)
    return habits

def delete_habit(user_id):
    """
    Enhanced deletion function:
    Displays one entry per habit (not per record),
    and includes start date and time in the list.
    """
    c.execute("SELECT habit_name, start_date, start_time FROM habits WHERE user_id=?", (user_id,))
    rows = c.fetchall()

    if not rows:
        print("No habits to delete.")
        return

    # Use a set to track unique (habit_name, start_date, start_time) combinations
    unique_habits = []
    seen = set()
    for name, date, time in rows:
        key = (name, date, time)
        if key not in seen:
            seen.add(key)
            unique_habits.append(key)

    # Show habits with index
    print("Select a habit to delete")
    for idx, (name, date, time) in enumerate(unique_habits, 1):
        print(f"{idx}. {name} | Start: {date} at {time}")

    try:
        choice = int(input("Enter number to delete: ")) - 1
        if 0 <= choice < len(unique_habits):
            name, date, time = unique_habits[choice]
            c.execute("DELETE FROM habits WHERE user_id=? AND habit_name=? AND start_date=? AND start_time=?",
                      (user_id, name, date, time))
            conn.commit()
            print(f"Habit '{name}' of {date} at {time} has been deleted successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")


"""This class, 'User', assigns user's information (from registration and habits dictionary)
   to variables including name, age, country, user_id, and habits."""
class User:
    #An '__init__' function for variables names for the class 'Habits'.
    def __init__(self, name, age, country, user_id):
        self.name = name
        self.age = age
        self.country = country
        self.user_id = user_id
        self.habits = []

    # This function appends the variable 'habits' in the __init__ function
    def add_habit(self, habit):
        self.habits.append(habit)

    """This function iterates 'habits' variable to assist deletion of habits."""
    """def delete_habit(self, habit_name):
            self.habits = [h for h in self.habits if h.name != habit_name]"""

"""This class, 'Habits', records habits data including habit's name, frequency,
   start_date, start_time."""
class Habit:
    #An '__init__' function for variables names for the class 'Habits'.
    def __init__(self, name, frequency, start_date, start_time):
        self.name = name
        self.frequency = frequency
        self.start_date = start_date
        self.start_time = start_time
        #This variable, 'records', provide a space to mark habit 30-times.
        self.records = [None] * 30

    """A function to assist marking 'yse' if a habits are completed."""
    def mark_complete(self, index):
        #Accessing the marking space.
        if 0 <= index < len(self.records):
            self.records[index] = True

    """A function to assist marking 'no' if a habits are completed."""
    def mark_incomplete(self, index):
        #Accessing the marking space.
        if 0 <= index < len(self.records):
            self.records[index] = False

    """This function, 'get_streaks()', compares data in 'records' variable
       to get longest and shortest streaks. Variables in this function assist
       'tracking()' function"""
    def get_streaks(self):
        longest = shortest = current = 0
        #Iterating 'records' variable to determine longest and shortest streaks.
        for day in self.records:
            if day:
                current += 1
                longest = max(longest, current)
            else:
                if current != 0:
                    shortest = min(shortest or current, current)
                current = 0
        return longest, shortest or 0






# IU-International University of Applied Sciences
# Course Code: DLBDSOOFPP01
# Author: Gabriel Manu
# Matriculation ID: 9212512