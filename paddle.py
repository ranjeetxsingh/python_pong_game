from turtle import Turtle
# Y 325 325
# X 425 425
MAX_UP_Y = 220
MIN_DOWN_Y = -220


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5.0, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < MAX_UP_Y:
            self.setposition(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > MIN_DOWN_Y:
            self.setposition(self.xcor(), self.ycor() - 20)

