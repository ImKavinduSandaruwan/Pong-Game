from turtle import Turtle
name = "Developed by Kavindu 😉"


class DevName(Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.hideturtle()
        self.penup()
        self.goto(0, -280)
        self.write(name, align="center", font=("Arial", 15, "bold"))
