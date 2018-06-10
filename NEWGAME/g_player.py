class Player(object):

    def __init__(self, username, years, gender):
        self.username = username
        self.years = years
        if gender is "m":
            self.gender = "boy"
        else:
            self.gender = "girl"
        self.score = 0

    def user_info(self):
        #print(self.username, self.years, self.gender, self.score)
        return self.username, self.years, self.gender, self.score

    def add_score(self):
        self.score += 1
        #print("Score is:", self.score)
