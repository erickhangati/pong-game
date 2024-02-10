from turtle import Turtle, Screen
from paddle import Paddle
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle_left = Paddle("left")
paddle_right = Paddle("right")

screen.update()

# Keep screen on
screen.exitonclick()
