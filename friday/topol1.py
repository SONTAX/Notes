from turtle import*
speed(0)
def square(length):
    color("gold")
    begin_fill()
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    end_fill()
def triangle(length):
    color("teal")
    begin_fill()
    forward(length)
    left(120)
    forward(length)
    left(120)
    forward(length)
    end_fill()
def house(length):
    triangle(length)
    left(30)
    square(length)
def background():
    color("blue")
    speed(30)
    goto(-200, +0)
    width(2000)
    forward(800)
    penup()
    width(200)
    goto(-250, - 200)
    pendown()
    color("green")
    forward(800)
    penup()
    goto(0, 0)
    pendown()
    width(1)
def window(length):
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length / 2)
    left(90)
    forward(length)
    left(90)
    forward(length / 2)
    left(90)
    forward(length / 2)
    left(90)
    forward(length)
def tree(length):
    color("brown")
    begin_fill()
    left(90)
    forward(length)
    left(90)
    forward(length / 3)
    left(90)
    forward(length)
    left(90)
    forward(length / 5)
    end_fill()
    left(90)
    forward(length)
    right(90)
    forward(length / 100)
    begin_fill()
    color("forestgreen")
    circle(length / 1.5)
    end_fill()
def fence(length):
    i = 0
    begin_fill()
    color("red")
    while i < 6:
        left(90)
        forward(length)
        right(45)
        forward(length / 3.3)
        right(90)
        forward(length / 3.3)
        right(45)
        forward(length)
        right(90)
        forward(length / 2.38)
        left(180)
        forward(length / 2.38)
        i = i + 1
    end_fill()
def star(length):
    begin_fill()
    color("yellow")
    i = 0
    while i < 5:
        forward(length)
        left(144)
        i = i + 1
    end_fill()
def sun(length):
    begin_fill()
    color("yellow")
    i = 0
    while i < 18:
        forward(length)
        left(100)
        i = i + 1
    end_fill()
def flower(length):
    color("green")
    width(length / 10)
    left(90)
    forward(length / 3)
    left(60)
    begin_fill()
    forward(length / 5)
    left(30)
    forward(length / 4)
    left(150)
    forward(length / 5)
    left(30)
    forward(length / 4)
    end_fill()
    left(90)
    forward(length / 2)
    penup()
    right(90)
    forward(length / 4)
    left(90)
    pendown()
    begin_fill()
    color("yellow")
    circle(length / 4)
    end_fill()
    penup()
    left(90)
    forward(length / 7)
    right(90)
    pendown()
    begin_fill()
    color("red")
    circle(length / 10)
    end_fill()
    width(1)


background()
house(100)
penup()
color("yellow")
forward(50)
left(90)
forward(70)
right(180)
pendown()
right(90)
pendown()
color("red")
forward(30)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(41)
left(90)
forward(22)
left(90)
forward(41)
penup()
left(90)
forward(23)
left(90)
pendown()
forward(21)
left(90)
forward(41)
penup()
left(90)
forward(120)
house(100)
penup()
color("yellow")
forward(50)
left(90)
forward(70)
right(180)
pendown()
right(90)
pendown()
color("red")
forward(30)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(41)
left(90)
forward(22)
left(90)
forward(41)
penup()
left(90)
forward(23)
left(90)
pendown()
forward(21)
left(90)
forward(41)
penup()
left(90)
forward(120)
house(100)
penup()
color("yellow")
forward(50)
left(90)
forward(70)
right(180)
pendown()
right(90)
pendown()
color("red")
forward(30)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(41)
left(90)
forward(22)
left(90)
forward(41)
penup()
left(90)
forward(23)
left(90)
pendown()
forward(21)
left(90)
forward(41)
penup()
left(90)
forward(120)
left(90)
forward(130)
forward(100)
left(90)
tree(100)
left(90)
forward(250)
sun(90)
left(180)
forward(200)
right(90)
forward(100)
flower(100)









































exitonclick()