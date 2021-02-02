from turtle import Turtle, Screen
import colorgram
import turtle as turtle_lodule
import random

# Extract 6 colors from an image.
def get_image_color_list(img_file):
    color_list = []
    colors = colorgram.extract(img_file, 20)
    for color in colors:
        color_list.append(tuple(color.rgb))

color_list = [(26, 108, 163), (228, 238, 231), (192, 39, 81), (235, 161, 54), (233, 215, 88), (221, 138, 176), (141, 108, 58), (104, 195, 217), (204, 165, 30), (21, 57, 131), (212, 75, 92), (236, 89, 50), (142, 208, 226), (119, 191, 141), (139, 29, 73), (9, 156, 88), (106, 108, 197)]
turtle_lodule.colormode(255)
tim = Turtle()
tim.speed(12)
tim.penup()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
dot_number = 100

for dot in range(1, dot_number+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()
screen = Screen()
screen.exitonclick()
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb
# print(tuple(rgb)) # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r