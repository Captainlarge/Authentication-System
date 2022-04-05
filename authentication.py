import sqlite3
import os
from time import sleep
from turtle import color
import format as format
import cfg
from termcolor import colored

access = False


def authenticate(hello):

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    # Initialising and Creating database
    hello = sqlite3.connect("userbase.db")
    hello.row_factory = dict_factory

    hello.execute('''CREATE TABLE if not exists LOGIN
                (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Email TEXT NOT NULL,
                Username TEXT NOT NULL,
                Password TEXT NOT NULL,
                First_Name TEXT NOT NULL,
                Last_Name TEXT NOT NULL);
                ''')
    hello.commit()

    # Adds user to userbase
    def register(hello):
        cfg.cls()
        print(format.REGISTER)
        first = input("")
        last = input("")
        email = input("")
        username = input("")
        password = input("")
        hello.execute("INSERT INTO LOGIN(Email, Username, Password,         First_Name, Last_Name) VALUES (?, ?, ?, ?, ?)", [
            email, username, password, first, last])
        hello.commit()
        cfg.cls()
        print(format.THANK)
        sleep(5)
        cfg.cls()
        return False, None

    # Determines whether login detail are allowed to access
    def login(hello):
        cfg.cls()
        print(format.LOGIN)
        inp_username = input("")
        inp_password = input("")
        current = hello.execute("SELECT First_Name, Last_Name FROM LOGIN WHERE Username = ? AND password = ?", [
            inp_username, inp_password]).fetchone()
        cfg.cls()
        if current != None:
            fn = current["First_Name"]
            ln = current["Last_Name"]
            print(colored(f'''
    ######################################################################################
    _       __     __                             ____             __   __
    | |     / /__  / /________  ____ ___  ___     / __ )____ ______/ /__/ /
    | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __  / __ `/ ___/ //_/ / 
    | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ / /_/ / /__/ ,< /_/  
    |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/  /_____/\__,_/\___/_/|_(_)   


    Nice to see you again, {fn} {ln}!

    ######################################################################################                                                              
            ''', "green"))
            sleep(7)
            cfg.cls()
            access = True
            return access, current
        elif current == None:
            print(format.UNSUCCESSFUL)
            sleep(3)
            access = False
            return access
        cfg.cls()

    # Calls the menu page
    cfg.cls()
    print(format.WELCOME)
    decision = input("Please make a selection: \n")
    cfg.cls()
    if decision == "1":
        return register(hello)
    if decision == "2":
        return login(hello)
