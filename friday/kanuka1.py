from turtle import *

speed(0)


def fon():
    goto(-500, 500)
    color("blue")
    width(2000)
    forward(1000)

    penup()
    goto(-500, -300)
    pendown()
    begin_fill()
    color("green")
    width(200)
    forward(5000)
    end_fill()


fon()


def day():
    penup()
    goto(150, 250)
    pendown()
    begin_fill()
    color("yellow")
    i = 0
    while i < 18:
        forward(100)
        left(100)
        i = i + 1
    end_fill()


day()
penup()
goto(-100, -200)


def square():
    color("red")
    begin_fill()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(180)
    forward(100)
    right(90)
    end_fill()
    color("black")
    begin_fill()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    end_fill()


square()
goto(100, -200)
left(120)
square()
goto(50, -200)
left(210)
pendown()


def derevo():
    color("brown")
    width(10)
    forward(100)
    color("green")
    width(100)
    forward(30)


derevo()
penup()
goto(-150, -200)
pendown()
derevo()
exitonclick()
