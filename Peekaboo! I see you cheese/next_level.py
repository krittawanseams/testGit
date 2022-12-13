from turtle import Turtle


class NextLevel(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('pink')
        self.penup()
        self.goto(x, y)

    def destroy(self):
        # self.goto(1000, 1000)
        self.hideturtle()
