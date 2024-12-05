import turtle
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard



my_screen = Screen()
my_screen.setup(height=600, width=600)
my_screen.bgcolor("black")
my_screen.title("Snake")
my_screen.listen()
my_screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
game_on = True


def end_game(x_cor, y_cor):
    if ((snake.head.xcor() > 290 or snake.head.xcor() < -290) or
            (snake.head.ycor() > 290 or snake.head.ycor() < -290)):
        score_board.reset_score()
        snake.reset_snake()

        return True
    else:
        return True

def score_and_snake_reset():
    score_board.reset_score()
    snake.reset_snake()
    food.move()


while game_on:
    my_screen.update()
    time.sleep(0.12)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        snake.add_tail_segment()
        score_board.increase_score()

    #Detect collision with wall
    #game_on = end_game(snake.head.xcor(), snake.head.ycor())
    if ((snake.head.xcor() > 290 or snake.head.xcor() < -290) or
            (snake.head.ycor() > 290 or snake.head.ycor() < -290)):
        score_and_snake_reset()


    #Detect collision with tail
    for segment in snake.snake_tail[1:]:
        if snake.head.distance(segment) < 10:
            score_and_snake_reset()

my_screen.exitonclick()
