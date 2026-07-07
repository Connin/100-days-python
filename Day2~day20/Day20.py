
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")

snake =[]
for i in range(0,3):
    tim = Turtle()
    tim.penup()
    tim.shape("square")
    tim.color("white")
    tim.goto(-20 * i,0)
    snake.append(tim)








screen.exitonclick()