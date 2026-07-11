from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ballx = 0
        self.bally = 0
        self.xbounce = 5
        self.ybounce = 5

    def move(self):
        self.ballx = self.xcor() + 5
        self.bally = self.ycor() + self.ybounce
        self.goto(self.ballx , self.bally)
        time.sleep(0.05)
        if self.ycor() > 280 or self.ycor() < -280:
            self.ybounce = -self.ybounce
    def bounce
    def padbounce(self):
