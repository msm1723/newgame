from . import g_rooms
from textwrap import dedent

class Menu(object):

    def __init__(self, player):
        self.player = player

    def room_select(self):
        username, years, gender, score = self.player.user_info()

        print(dedent(f"""
            User info:
            - Username: {username}
            - Age: {years}
            - Gender: {gender}
            - Score: {score}
            """))

        print(dedent(f"""
            So {username} you entering in to the stupidy check facility.
            You need to get success in all rooms to prove you are not stupid.
            So select room number you'd like to begin with:
            1 Geometry
            2 History
            3 Astronomy
            4 Phylosophy
            5 Poetry
            """))

        while True:
            room_choice = input('> ')
            try:
                room_number = int(room_choice)
            except:
                print("So stupid, can't type a number?")
                continue
            if room_number == 0:
                love()
            elif room_number not in range(1, 5):
                print("Number between 1 and 5, genious!")
                continue
            elif room_number == 1:
                return g_rooms.Geometry(self.player)
            elif room_number == 2:
                return g_rooms.History(self.player)
#            elif room_number == 3:
#                return Astronomy(player)
#            elif room_number == 4:
#                return Phylosophy(player)
#            elif room_number == 5:
#                return Poetry(player)
