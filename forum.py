from termcolor import colored
import sqlite3
import os
from time import sleep
from turtle import color
import authentication
import cfg
import format


access = False

# Verifying login status
hello = sqlite3.connect("userbase.db")
while True:
    access, current_user = authentication.authenticate(hello)
    if access == True:
        user_id = current_user["ID"]
        break


# Initialise POSTS database

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


forum = sqlite3.connect("userbase.db")
forum.row_factory = dict_factory


forum.execute('''CREATE TABLE if not exists POSTS
                (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                User_ID INTEGER NOT NULL,
                Title TEXT NOT NULL,
                Body TEXT NOT NULL,
                Date DATETIME NOT NULL);
                ''')
forum.commit()


def home(forum):
    cfg.cls()
    print(format.HOME)
    decision = input("Please make a selection: \n")
    cfg.cls()
    if decision == "1":
        viewPost(forum)
    if decision == "2":
        createPost(forum)
    if decision == "3":
      deletePost(forum)


def createPost(forum):
    cfg.cls()
    print(format.CREATE)
    title = input("")
    body = input("")
    date = input("")
    forum.execute("INSERT INTO POSTS(User_ID, Title, Body, Date) VALUES (?, ?, ?, ?)", [
        user_id, title, body, date])
    forum.commit()
    cfg.cls()
    print(format.THANK)
    sleep(3)
    cfg.cls()
    home(forum)


def viewPost(forum):
    current = forum.execute("SELECT * FROM POSTS").fetchall()
    print(format.VIEW)
    for x in range(len(current)):
        user = forum.execute("SELECT * FROM LOGIN WHERE ID = ?", [current[x]["User_ID"]]).fetchall()
        print(colored(current[x]["Title"], "blue", attrs=["bold"]))
        print(colored(current[x]["Body"], "blue"))
        p = user[0]["First_Name"]
        print(colored(f"By {p}", "blue", attrs=["dark"]))
    print(colored('''
Press enter to go back
######################################################################################
    ''', "blue"))
    input("")
    home(forum)



def deletePost(forum):
  current = forum.execute("SELECT * FROM POSTS WHERE user_ID = ?", [user_id]).fetchall()
  for x in range(len(current)):
    print(current[x]["Title"])
    print("Please enter title of the post you wish to delete:")
    forum.execute("DELETE FROM POSTS WHERE Title = ?", [chosen])

  
home(forum)
