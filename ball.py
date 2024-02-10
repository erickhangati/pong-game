from turtle import Turtle, textinput
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.game_on = False
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")
        self.penup()
        self.start_ball()
        self.x_move = 10
        self.y_move = 10

    def start_ball(self):
        """
        Start ball movement.
        :return: None
        """
        start_game = textinput("Pong", "Enter YES to start")
        if start_game.lower() == "yes":
            self.game_on = True

    def move_ball(self):
        """
        Move the ball
        :return: None
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
