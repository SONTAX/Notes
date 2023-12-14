from turtle import *

t = Turtle()
t.color("blue")
t.shape("turtle")
t.width(4)
t.down()
t.speed(0)
def star():
    t.begin_fill()
    i = 0
    while i < 5:
        t.forward(40)
        t.left(144)
        i = i + 1
    t.end_fill()
def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def crimson():
    t.color("crimson")
def white():
    t.color("white")

def aqua():
    t.color("aqua")

def blue():
    t.color("blue")

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
screen.onkey(crimson, "1")
screen.onkey(aqua, "2")
screen.onkey(blue, "3")
screen.onkey(t.begin_fill, "b")
screen.onkey(t.end_fill, "e")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(star, "4")
screen.onkey(white, "5")


t3 = Turtle()
t3.width(2000)
t3.color("black")
t3.forward(1)
t3.hideturtle()
