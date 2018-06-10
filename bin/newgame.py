#! /usr/bin/env python

# entry point for the game

# impopt module
# import <package>
# import <module>
# from <package> import <module or subpackage or object>
# from <module> import <object>

from NEWGAME import g_player
from NEWGAME import g_menu
from NEWGAME import g_rooms

def createUser():

    print("Hello, mortal...")

    while True:
        print("What's your name?")
        username = input('>> ')
        try:
            if not username.strip():
                raise ValueError("Let's try again!")
            break
        except ValueError as e:
            print(e)

    while True:
        print("How old are you?")
        years = input('>> ')
        try:
            years = int(years)
            break
        except:
            print("Not a number. Try again!")

    while True:
        print("Man or woman [m/w]?")
        gender = input('>> ')
        try:
            if gender not in ("m", "w"):
                raise ValueError("Try again!")
            break
        except ValueError as e:
            print(e)

    return g_player.Player(username, years, gender)

player = createUser()

menu = g_menu.Menu(player)

while player.score < 5:
    current_room = menu.room_select()
    current_room.run()
