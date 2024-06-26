from turtle import Screen
import time
from utils.snake import Snake
from utils.food import Food
from utils.scoreboard import ScoreBoard
import math



screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('My Snake Game')
screen.listen()

snake = Snake()
food = Food()
food.refresh()
scoreboard = ScoreBoard()
scoreboard.display_score()

screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_right, 'Right')
screen.onkey(snake.turn_down, 'Down')


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision using pos() method
    snake_x, snake_y = snake.get_first_pos()
    food_x, food_y = food.pos()
    if abs(snake_x - food_x) <= 15 and abs(snake_y - food_y) <= 15:
        food.refresh()
        snake.add_segment()
        scoreboard.update_score()
        scoreboard.refresh_scoreboard()

    # If snake hit the boundary
    if snake_x > 280 or snake_x < -280 or snake_y > 280 or snake_y <-280 :
        scoreboard.reset_score()
        snake.restart_game()
    # If snake hit itself
    for segment in snake.segments[1:]:
        if snake.head().distance(segment) < 10:
            scoreboard.reset_score()
            snake.restart_game()

screen.exitonclick()