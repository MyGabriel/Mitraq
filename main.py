# File: main

"""Importing classes and functions from other Mitraq files"""
from mitraq_classes import dashboard, habit_menu
import mitraqdb
from mitraqdb import User
import analysis

# This function, 'main()', initiates the Mitraq program. It invokes 'dashboard()',
# 'register()', and 'login()' functions.
def main():

    while True:
        # Printing Mitraq's welcome message
        print(f"\n{"_"*10}| WELCOME TO MITRAQ |{"_"*10}\n1. Register\n2. Login\n3. Quit")
        choice = input("Choose option: ")
        if choice == '1':
            mitraqdb.register()
        elif choice == '2':
            user = mitraqdb.login()
            if user:
                dashboard(user)
        elif choice == '3':
            print("\nThank you for using Mitraq, see you again.")
            break

# Controlling code execution with the '__name__' variable.
if __name__ == "__main__":
    """Invoking the 'main' function above."""
    main()





# IU-International University of Applied Sciences
# Course Code: DLBDSOOFPP01
# Author: Gabriel Manu
# Matriculation ID: 9212512