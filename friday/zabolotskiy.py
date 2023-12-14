from turtle import *
from random import *

t = Turtle()
t.color("gold")
t.shape("turtle")
t.width(7)
t.down()
t.speed(0)


def draw(x, y):
    t.goto(x, y)


def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def olive():
    t.color("olive")


def purple():
    t.color("purple")


def gold():
    t.color("gold")


def blue():
    t.color("blue")


def red():
    t.color("red")


def green():
    t.color("green")


def begin():
    t.begin_fill()


def begin():
    t.end_fill()


def move_up():
    t.goto(t.xcor(), t.ycor() + 5)


def move_down():
    t.goto(t.xcor(), t.ycor() - 5)


def move_left():
    t.goto(t.xcor() - 5, t.ycor())


def move_right():
    t.goto(t.xcor() + 5, t.ycor())


def star():
    for _ in range(5):
        t.forward(30)
        t.left(144)


t.ondrag(draw)
screen = t.getscreen()
screen.onscreenclick(move)
screen.listen()
screen.onkey(olive, "1")
screen.onkey(purple, "2")
screen.onkey(gold, "3")
screen.onkey(blue, "4")
screen.onkey(red, "5")
screen.onkey(green, "6")
screen.onkey(t.begin_fill, "b")
screen.onkey(t.end_fill, "e")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(star, "9")
