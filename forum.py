import sqlite3
import os
from time import sleep
from turtle import color
import Authentication.format as format
import Authentication.Config.cfg as cfg
from termcolor import colored
import Authentication.authentication as authentication

# Verifying login status
hello = sqlite3.connect("userbase.db")
while True:
    access = authentication.authenticate(hello)
    if access == True:
        break
