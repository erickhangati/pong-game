from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.scores = 0
        self.position = position
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.set_position()
        self.color("white")
        self.display_score()

    def set_position(self):
        """
        Set the position of the scores.
        :return: None
        """
        if self.position == "left":
            self.goto(-200, 280)
        else:
            self.goto(200, 280)

    def display_score(self):
        """
       Display contact on screen
       :return: None
       """
        self.write(f"Scores: {self.scores}", font=('Courier', 12, "normal"), align="center")

    def update_scores(self):
        self.clear()
        self.scores += 1
        self.display_score()
