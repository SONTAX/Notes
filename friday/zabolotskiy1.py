from turtle import *

exitonclick()
color("light blue")
speed(30)
goto(-200, +0)
width(2000)
forward(800)
penup()
width(200)
goto(-250, -200)
pendown()
color("dark blue")
forward(800)
penup()
goto(-250, -100)
color("sienna")
pendown()
width(50)
forward(800)
width(1)
penup()
goto(200, 100)
width(1)
lenght = int(input())


def star(length):
    begin_fill()
    color("yellow")
    for i in range(12):
        forward(lenght)
        left(180 - 30)
    end_fill()


pendown()
star(100)
penup()
goto(-200, -150)


def ship():
    begin_fill()
    color("white")
    width(4)
    forward(50)
    left(135)
    forward(70)
    left(135)
    forward(50)
    end_fill()

    begin_fill()
    color("black")
    width(3)
    right(90)
    forward(50)
    left(135)
    forward(50)
    left(45)
    forward(80)
    left(45)
    forward(50)
    left(135)
    forward(110)
    left(180)
    end_fill()


pendown()

ship()
penup()
goto(+0, -150)
pendown()
ship()
penup()
goto(-200, 0)
pendown()


def house():
    begin_fill()
    right(90)

    forward(80)
    left(90)
    forward(80)
    left(90)
    forward(80)
    left(90)
    forward(80)

    right(120)
    forward(80)
    right(120)
    forward(80)
    left(60)
    end_fill()


color("firebrick")
house()
penup()
forward(50)
pendown()
house()
penup()
forward(50)
pendown()
house()
penup()
forward(50)
