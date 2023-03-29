# Login System
This code is a simple login system built with the FastAPI framework. The system allows users to login with their username and password, and records the login time in a SQLite database.

## Requirements
In order to run this code, you must have Python 3 installed, along with the following packages:

FastAPI
Pydantic
SQLAlchemy
SQLite3
You can install these packages by running ```pip install -r requirements.txt``` in your terminal.

## Usage
Activate your virtual environment by running source venv/bin/activate in your terminal.

Run the code by typing uvicorn main:app --reload in your terminal.

Navigate to ```http://localhost:8000/static/index.html```

If the username and password are correct, the API will return a JSON response with "success": true, and the login time will be recorded in the database. If the username and password are incorrect, the API will return "success": false.

## Database
The system uses a SQLite database to store the user information and login times. When you run the code, a database file called "login.db" will be created in the same directory as the code.

The users table contains the following columns:

id (integer, primary key)
username (text)
password (text)
The login_info table contains the following columns:

id (integer, primary key)
username (text)
login_time (text)
The system checks if the default admin user exists in the database on startup, and adds it if it doesn't exist. The default admin username and password are both "admin".
