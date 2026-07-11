from turtle import Turtle, Screen

#turt.write((0,0), False)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", "center", font=('Arial', 20, 'normal'))

