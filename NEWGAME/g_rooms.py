# rooms
from itertools import count

class Room(object):
    _total_rooms_count = count(1)
    _geometry_rooms_visited = count(1)
    _history_rooms_visited = count(1)

    def __init__(self, room_type):

        self.total_rooms_count = next(self._total_rooms_count)
        print(f"Total rooms visited: {self.total_rooms_count}")
        if room_type is 'Geometry':
            self.geometry_rooms_visited = next(self._geometry_rooms_visited)
            print(f"Geometry rooms visited: {self.geometry_rooms_visited}")
        elif room_type is 'History':
            self.history_rooms_visited = next(self._history_rooms_visited)
            print(f"History rooms visited: {self.history_rooms_visited}")
        else:
            print("Else")


# Geometry room
class Geometry(Room):

    def __init__(self, player):
        self.room_type = 'Geometry'
        Room.__init__(self, self.room_type)

        self.player = player

    def run(self):
        username, _, _, score = self.player.user_info()

        print(f"Well, {username}, you score is {score}. Choose a number please:",)

        while True:
            number = input('>> ')
            try:
                number = int(number)
                break
            except:
                print("So stupid, can't type a number?")
                continue

        import math
        cirqle_area = math.pi * number * number
        print(cirqle_area)

        print(f"What area cirqle have if radius is {number}?")

        while True:
            answer = input('>> ')
            try:
                answer = float(answer)
            except:
                print("Try again!")
                continue

            if answer == cirqle_area:
                print("Not bad. Scored! Go on select another room!")
                self.player.add_score()
                break
            else:
                print("Wrong. Please try harder.")

# History room
class History(Room):

    def __init__(self, player):
        self.room_type = 'History'
        Room.__init__(self, self.room_type)

        self.player = player

    def run(self):
        username, _, _, score = self.player.user_info()
        print(f'Hello {username}, your score is {score}')
        Q1 = [1, "A true personal name, chosen by a child's parents"]
        A1 = [1, "Praenomen"]
        Q2 = [2, 'Designated a Roman citizen as a member of a gens, which may be translated as "race", "family", or "clan".']
        A2 = [2, "Nomen"]
        Q3 = [3, "The third element of the tria nomina, began as an additional personal name."]
        A3 = [3, "Cognomen"]
        all_questions = [Q1, Q2, Q3]
        all_answers = [A1, A2, A3]


        print(f"Well, {username}, please read Roman name definition: ")
        import random
        question = random.choice(all_questions)
        print(question[1])

        while True:
            print("What name is it?")
            print("1", all_answers[0][1])
            print("2", all_answers[1][1])
            print("3", all_answers[2][1])

            while True:
                keyboard = input('>> ')
                try:
                    answer = int(keyboard)
                    break
                except:
                    print("So stupid, can't type a number?")
                    continue

            if answer == question[0]:
                print("Not bad. Scored! Go on select another room!")
                self.player.add_score()
                break
            else:
                print("Wrong. Please try harder.")
                continue
