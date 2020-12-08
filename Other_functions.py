# import only system from os
from os import system, name


def clear():
    """Clears the terminal/command prompt screen"""
    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For MAC and Linux(here, os.name is 'posix')
    else:
        _ = system('clear')
