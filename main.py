from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import keyboard

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_on = False
while not game_on:
    if keyboard.is_pressed("right"):
        game_on = True
    elif keyboard.is_pressed("up"):
        snake.left()
        game_on = True
    elif keyboard.is_pressed("down"):
        snake.right()
        game_on = True
    my_screen.update()

while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        scoreboard.reset_game()
        snake.reset_snake()

    for seg in snake.segments:
        if snake.head.distance(seg) < 10 and seg != snake.head:
            scoreboard.reset_game()
            snake.reset_snake()


my_screen.exitonclick()
