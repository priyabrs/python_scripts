from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, color = 'blue') -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color(color)
        self.speed('fastest')
        
    def reset_food(self) -> None:
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)


# f = Food()