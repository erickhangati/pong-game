from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

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
    # Move ball
    ball.forward(10)

    # Detect wall collision and update scores
    if ball.xcor() >= 385:
        scores_left.update_scores()
        break
    elif ball.xcor() <= -400:
        scores_right.update_scores()
        break

    if ball.distance(paddle_right) < 10 or ball.distance(
            paddle_left) < 10 or ball.ycor() >= 290 or ball.ycor() <= -280:
        ball.setheading(360 - ball.heading())
        # break

# Keep screen on
screen.exitonclick()
