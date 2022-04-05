# Modules
import os

# Constants

# Functions


def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
