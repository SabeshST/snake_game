import turtle
from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_tail = []
        self.create_snake()


        turtle.onkeypress(key="Up", fun=self.turn_up)
        turtle.onkeypress(key="Down", fun=self.turn_down)
        turtle.onkeypress(key="Left", fun=self.turn_left)
        turtle.onkeypress(key="Right", fun=self.turn_right)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset_snake(self):
        for i in self.snake_tail:
            i.teleport(1000,1000)
        self.snake_tail.clear()
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.snake_tail[0]
        self.head.color("Blue")

    def add_segment(self, position):
        tail_turtle = Turtle()
        tail_turtle.shape("square")
        tail_turtle.penup()
        tail_turtle.color("white")
        tail_turtle.speed(1)
        tail_turtle.goto(position)
        self.snake_tail.append(tail_turtle)

    def move(self):
        for i in range(len(self.snake_tail) - 1, 0, -1):
            new_x = self.snake_tail[i - 1].xcor()
            new_y = self.snake_tail[i - 1].ycor()
            self.snake_tail[i].goto(new_x, new_y)
        self.snake_tail[0].forward(MOVE_DISTANCE)

    def add_tail_segment(self):
        self.add_segment(self.snake_tail[-1].pos())
