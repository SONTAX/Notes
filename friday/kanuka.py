from turtle import *

t1 = Turtle()
t1.color("red")
t1.shape("circle")
t1.width(5)
t1.down()
t1.speed(0)


def move(x, y):
    t1.up()
    t1.goto(x, y)
    t1.down()


def draw(x, y):
    t1.goto(x, y)


def blue():
    t1.color("blue")


def red():
    t1.color("red")


def green():
    t1.color("green")


def purple():
    t1.color("purple")


def yellow():
    t1.color("yellow")


def black():
    t1.color("black")


def pink():
    t1.color("pink")


def begin():
    t1.begin_fill()


def end():
    t1.end_fill()


def mowe_up():
    t1.goto(t1.xcor(), t1.ycor() + 5)


def mowe_left():
    t1.goto(t1.xcor() - 5, t1.ycor())


def mowe_down():
    t1.goto(t1.xcor(), t1.ycor() - 5)


def mowe_right():
    t1.goto(t1.xcor() + 5, t1.ycor())


def square():
    for i in range(360):
        t1.forward(1)
        t1.left(1)


def kvadrat():
    for i in range(4):
        t1.forward(100)
        t1.left(90)


t1.ondrag(draw)
screen = t1.getscreen()
screen.listen()
screen.onscreenclick(move)
screen.onkey(blue, "1")
screen.onkey(red, "2")
screen.onkey(green, "3")
screen.onkey(purple, "4")
screen.onkey(yellow, "5")
screen.onkey(black, "6")
screen.onkey(pink, "7")
screen.onkey(square, "v")
screen.onkey(kvadrat, "k")
screen.onkey(begin, "q")
screen.onkey(end, "e")
screen.onkey(mowe_up, "w")
screen.onkey(mowe_left, "a")
screen.onkey(mowe_down, "s")
screen.onkey(mowe_right, "d")
