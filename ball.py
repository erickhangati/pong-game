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
        self.speed(1)
        self.start_ball()
        self.setheading(randint(0, 360))

    def start_ball(self):
        """
        Start ball movement.
        :return: None
        """
        start_game = textinput("Pong", "Enter YES to start")
        if start_game.lower() == "yes":
            self.game_on = True
