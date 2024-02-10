from turtle import Turtle


class Paddle(Turtle):
    x = 0
    y = 0

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.set_side()
        self.goto(self.x, self.y)
        self.setheading(90)

    def set_side(self):
        if self.position == "left":
            self.x = -390
        else:
            self.x = 380
