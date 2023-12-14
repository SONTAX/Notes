from turtle import *

t = Turtle()
t.color("gold")
t.shape("turtle")
t.width(3)
t.down()
t.speed(0)


def draw(x, y):
    t.goto(x, y)


def house():
    for _ in range(3):
        t.forward(50)
        t.left(120)
    t.right(90)
    for _ in range(4):
        t.forward(50)
        t.left(90)
    t.left(90)


def green():
    t.color("green")


def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def olive():
    t.color("olive")


t.ondrag(draw)
screen = t.getscreen()
screen.onscreenclick(move)
screen.onkey(olive, "1")
screen.listen()
screen.onkey(green, "2")
screen.onkey(house, "3")




