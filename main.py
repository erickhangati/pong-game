from turtle import Screen
from paddle import Paddle
from ball import Ball

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# Paddle instances
paddle_left = Paddle("left")
paddle_right = Paddle("right")

# Ball instance
ball = Ball()

# Listen for strokes
screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

game_on = ball.game_on

while game_on:
    ball.forward(10)

    if ball.xcor() >= 385 or ball.xcor() <= -400:
        break

# Keep screen on
screen.exitonclick()
