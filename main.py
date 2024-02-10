from turtle import Screen, textinput
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


def switch_off():
    global game_on
    game_on = False


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

# Player names
player_1 = textinput("Player 1", "Enter player 1's name")
if player_1:
    scores_left.name = player_1
    scores_left.update_names()

player_2 = textinput("Player 2", "Enter player 2's name")
if player_2:
    scores_right.name = player_2
    scores_right.update_names()

# Listen for strokes
screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)
screen.onkey(key="space", fun=switch_off)

game_on = True

while game_on:
    screen.update()
    sleep(0.1)

    # Move ball
    ball.move_ball()

    # Contact with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 360 or ball.distance(
            paddle_left) < 50 and ball.xcor() < -370:
        ball.bounce_paddle()

    # Detect side walls collision, update scores & reset position
    if ball.xcor() >= 385:
        scores_left.update_scores()
        ball.reset_position()
        ball.bounce_paddle()
        ball.bounce_wall()
    elif ball.xcor() <= -400:
        scores_right.update_scores()
        ball.reset_position()
        ball.bounce_paddle()
        ball.bounce_wall()

    # Collision with top/bottom walls
    if ball.ycor() >= 290 or ball.ycor() <= -280:
        ball.bounce_wall()

# Keep screen on
screen.exitonclick()
