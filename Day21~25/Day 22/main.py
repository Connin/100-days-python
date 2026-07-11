from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()


# ballx = 0
# bally = 0

# ball.shape("circle")
# ball.color("white")
# ball.penup()
# screen.update()
# for i in range(0, 200):
#     ball.goto(ballx , bally)
#     ballx += 4
#     bally += 4
#     time.sleep(0.02)
#     screen.update()

screen.listen()
screen.onkeypress(r_paddle.goup, "Up")
screen.onkeypress(r_paddle.godown, "Down")
screen.onkeypress(l_paddle.goup, "w")
screen.onkeypress(l_paddle.godown, "s")
screen.update()

game_is_on = True
while game_is_on:
     screen.update()
     ball.move()
     if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
          print('contact')
#     time.sleep(0.02)
# #     snake.move()
# #     if snake.head.distance(food) < 15:
# #         food.refresh()

screen.exitonclick()