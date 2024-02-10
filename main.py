from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Scores
scores_left = Scoreboard("left")
scores_right = Scoreboard("right")

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
    screen.update()
    sleep(0.1)

    # Move ball
    ball.move_ball()

    # Contact with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 360 or ball.distance(
            paddle_left) < 50 and ball.xcor() < -370:
        ball.bounce_paddle()

    # Detect side walls collision and update scores
    if ball.xcor() >= 385:
        scores_left.update_scores()
        break
    elif ball.xcor() <= -400:
        scores_right.update_scores()
        break

    # Collision with top/bottom walls
    if ball.ycor() >= 290 or ball.ycor() <= -280:
        ball.bounce_wall()

# Keep screen on
screen.exitonclick()
