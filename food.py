from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(0.5, 0.5)
        self.move()

    def move(self):
        random_x_spot = random.randint(-280, 280)
        random_y_spot = random.randint(-280, 280)
        self.teleport(random_x_spot, random_y_spot)