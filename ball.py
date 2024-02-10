from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        """
        Move the ball
        :return: None
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        """
        Bounce ball when in contact with top/bottom walls.
        :return: None
        """
        self.y_move *= -1

    def bounce_paddle(self):
        """
        Bounce ball when in contact with paddles walls.
        :return: None
        """
        self.x_move *= -1

    def reset_position(self):
        """
        Reset position after collision with walls.
        :return: None
        """
        sleep(2)
        self.goto(0, 0)
