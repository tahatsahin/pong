from turtle import Turtle

STARTING_POSITIONS1 = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
STARTING_POSITIONS2 = [(-350, 40), (-350, 20), (-350, 0), (-350, -20), (-350, -40)]


class Paddle(Turtle):

    def __init__(self, center):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(center)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

