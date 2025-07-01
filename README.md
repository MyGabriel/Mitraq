# MiTraq


---
## About Mitraq
Mitraq is a habit tracker built with Python’s object-oriented and functional programming concepts. 
It is text-base (CLI) and lightweight (without graphics). Can be used without internet.
Mitraq uses SQLite3 for data operations.

The Mitraq is built with a five-predefined habits and users have the ability to design or customize
a suitable habit. The customisation access in the application allows a user to design a habit to 
build or break. The idea is for the user to intentionally login into the application to track progress (either 
building or breaking habits). 
Note: Each user has a unique code given during registration: Used for logins. 
---

## Features
- Secure user registration with unique ID
- Habit creation (default or custom)
- Daily and weekly tracking
- Visual tracking summary (✔ = complete, ✘ = missed, _ = unmarked)
- Habit deletion
- Analytics: longest and shortest streaks

---

## Mitraq's Flowchart
Use the link below to access how Mitraq components flow.
https://github.com/MyGabriel/Mitraq/blob/main/Mitraq%20FlowChart.png?raw=true


## Installation
1. Clone the repository:
```bash
git clone https://github.com/MyGabriel/Mitraq.git
```

2. Run the app:
```bash
python main.py
```

---

## Running Tests
Make sure you have Python 3.10+ installed, then run:
```bash
pytest 
```
---