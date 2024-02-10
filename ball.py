from turtle import Turtle, textinput


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.game_on = False
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")
        self.penup()
        self.speed(3)
        self.start_ball()
        self.setheading(180)

    def start_ball(self):
        start_game = textinput("Pong", "Enter YES to start")
        if start_game.lower() == "yes":
            self.game_on = True
