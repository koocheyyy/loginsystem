from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from datetime import datetime


import sqlite3

app = FastAPI()

app.mount("/static", StaticFiles(directory=Path(__file__).parent.absolute() / "static"), name="static")

class LoginRequest(BaseModel):
    username: str
    password: str

# create a connection to the database
conn = sqlite3.connect('login.db')
c = conn.cursor()

# create a table to store the users
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

# check if the default admin user exists in the database, and add it if it doesn't
c.execute('SELECT * FROM users WHERE username = ?', ('admin',))
if not c.fetchone():
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'admin'))
    conn.commit()

# create a table to store the login information
c.execute('CREATE TABLE IF NOT EXISTS login_info (id INTEGER PRIMARY KEY, username TEXT, login_time TEXT)')

Base = declarative_base()
class Login(Base):
    __tablename__ = 'logins'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(request: Request, login_request: LoginRequest):
    data = login_request.dict()
    username = data['username']
    password = data['password']
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = c.fetchone()
    if result:
        # record the login information in the database
        c.execute('INSERT INTO login_info (username, login_time) VALUES (?, ?)', (username, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        return {"success": True}
    else:
        return {"success": False}
