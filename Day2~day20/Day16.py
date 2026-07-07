# import another_module
# print(another_module.another_variable)

#from turtle import Turtle
import turtle

timmy = turtle.Turtle()
my_screen = turtle.Screen()

# turtle = 모듈
# Turtle = 클래스
# timmy = 객체(object)
# 객체 = 모듈.클래스()
# 객체.메서드()
# turtle (모듈)
# │
# ├── Turtle (클래스)(설계도)
# │   ├── shape()      ← 메서드
# │   ├── color()      ← 메서드

print(turtle.Turtle())
timmy.shape("turtle")
timmy.color("DeepSkyBlue")
timmy.forward(100)


print(my_screen.canvheight)
my_screen.exitonclick()