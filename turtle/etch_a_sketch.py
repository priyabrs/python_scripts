from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def turn_up():
    tim.setheading(90)

def turn_down():
    tim.setheading(270)

def create_circle():
    tim.circle(120)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, 'space')
screen.onkey(turn_left, 'Left')
screen.onkey(turn_right, 'Right')
screen.onkey(turn_up, 'Up')
screen.onkey(turn_down, 'Down')
screen.onkey(create_circle, 'o')
screen.onkey(clear, 'c')
screen.exitonclick()