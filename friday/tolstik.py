from turtle import *

# start
t = Turtle()
t.color("black")
t.shape("turtle")
t.width(10)
t.down()
t.speed(0)
t.w = 5


def draw(x, y):
    t.goto(x, y)


def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()


# zveta
def darkorange():
    t.color("darkorange")


def black():
    t.color("black")


def maroon():
    t.color("maroon")


# zalivka
def begin():
    t.begin_fill()


def end():
    t.end_fill()


# dvizeniye
def move_up():
    t.goto(t.xcor(), t.ycor() + 5)


def move_down():
    t.goto(t.xcor(), t.ycor() - 5)


def move_left():
    t.goto(t.xcor() - 5, t.ycor())


def move_right():
    t.goto(t.xcor() + 5, t.ycor())


# tolshina
def width1():
    t.w += 5
    t.width(t.w)
    print(t.w)


def width2():
    t.w -= 5
    t.width(t.w)
    print(t.w)


# start
t.ondrag(draw)

screen = t.getscreen()
screen.onscreenclick(move)
# bind zveta
screen.onkey(maroon, "1")
screen.listen()
screen.onkey(darkorange, "2")
screen.onkey(black, "3")
# bind zalivki
screen.onkey(t.begin_fill, "b")
screen.onkey(t.end_fill, "e")
# bind dvizeniya
screen.onkey(move_up, "up")
screen.onkey(move_down, "down")
screen.onkey(move_left, "left")
screen.onkey(move_right, "right")
# bind tolshina
screen.onkey(width1, "6")
screen.onkey(width2, "5")