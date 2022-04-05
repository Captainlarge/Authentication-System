from termcolor import colored
import sqlite3
import os
from time import sleep
from turtle import color
import authentication
access = False

# Verifying login status
hello = sqlite3.connect("userbase.db")
while True:
    access, current_user = authentication.authenticate(hello)
    if access == True:
        break

print(current_user)

# Initialise POSTS database
forum = sqlite3.connect("userbase.db")
hello.execute('''CREATE TABLE if not exists POSTS
                (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                User_ID INTEGER NOT NULL,
                Title TEXT NOT NULL,
                Body TEXT NOT NULL,
                Date DATETIME NOT NULL);
                ''')
hello.commit()
