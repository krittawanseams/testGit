from turtle import Turtle


class Cheese(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape('cheese2.gif')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.cheese = 1
        self.goto(x, y)

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()
