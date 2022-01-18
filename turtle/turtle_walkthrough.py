import random
from turtle import Turtle, Screen
import turtle

def draw_shape(object):
    object_sides = {'triangle':3, 'square':4, 'pentagon':5, 'hexagon':6, 'octagon':8, 'decagon':10, 'circle':120}
    sides = object_sides[object]
    timmy = Turtle()
    timmy.shape('turtle')
    timmy.color('red')
    degree = 360/sides
    for _ in range(sides):
        timmy.forward(80)
        timmy.left(degree)

def random_color():
    r_red = random.randint(0,255)
    r_green = random.randint(0,255)
    r_blue = random.randint(0,255)
    return (r_red, r_green, r_blue)

def random_walk():
    # color_list = ['red', 'azure', 'brown', 'DeepPink','DeepSkyBlue', 'lawngreen', 'gold1','navy']
    turtle.colormode(255)
    timmy = Turtle()
    timmy.speed(7)
    timmy.pensize(8)
    directions = [0, 90, 180, 270]
    for _ in range(200):
        timmy.color(random_color())
        timmy.forward(20)
        timmy.setheading(random.choice(directions))

def draw_spirograph(gap_size):
    turtle.colormode(255)
    timmy = Turtle()
    timmy.speed(15)
    for _ in range(int(360/gap_size)):
        timmy.color(random_color())
        timmy.circle(120)
        timmy.setheading(timmy.heading() + gap_size)

draw_spirograph(10)

# timmy = Turtle()
# timmy.color('red')
# timmy.circle(120, 360)
# timmy.position()
# timmy.color('blue')
# timmy.circle(120, 360)
# screen = Screen()
# screen.exitonclick()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()