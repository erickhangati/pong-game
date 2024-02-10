from turtle import Turtle


class Paddle(Turtle):
    x = 0
    y = 0

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.set_side()
        self.goto(self.x, self.y)
        self.setheading(90)
        self.showturtle()

    def set_side(self):
        """
        Set paddle side.
        :return: None
        """
        if self.position == "left":
            self.x = -390
        else:
            self.x = 380

    def move_up(self):
        """
        Move the paddle up.
        :return: None
        """
        if not self.ycor() >= 250:
            self.setheading(90)
            self.forward(20)

    def move_down(self):
        """
        Move the paddle down.
        :return: None
        """
        if not self.ycor() <= -230:
            self.setheading(270)
            self.forward(20)
