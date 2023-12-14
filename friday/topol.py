from turtle import *

t = Turtle()
t.color("gold")
t.shape("turtle")
t.width(4)
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

def grey():
    t.color("grey")

def slategrey():
    t.color("slategrey")

def snow():
    t.color("snow")

def dimgray():
    t.color("dimgray")




def move_up():
    t.goto(t.xcor(), t.ycor() + 15)


def move_down():
    t.goto(t.xcor(), t.ycor() - 15)


def move_left():
    t.goto(t.xcor() - 15, t.ycor())


def move_right():
    t.goto(t.xcor() + 15, t.ycor())


t.ondrag(draw)
screen = t.getscreen()
screen.onscreenclick(move)
screen.listen()
screen.onkey(olive, "1")
screen.onkey(purple, "2")
screen.onkey(gold, "3")
screen.onkey(grey, "4")
screen.onkey(slategrey, "5")
screen.onkey(snow, "6")
screen.onkey(dimgray, "7")
screen.onkey(t.begin_fill, "b")
screen.onkey(t.end_fill, "e")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
