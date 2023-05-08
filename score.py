from turtle import Turtle


class ScoreBoad(Turtle):

    def __init__(self):
        super().__init__()
        self.color('green')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_score()