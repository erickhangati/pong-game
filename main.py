from turtle import Turtle, Screen
from paddle import Paddle

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(2)

# Paddle instances
paddle_left = Paddle("left")
paddle_right = Paddle("right")

# Listen for strokes
screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

# Keep screen on
screen.exitonclick()
