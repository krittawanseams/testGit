import random
from turtle import Turtle


class Enemy(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape('cat_right.gif')
        self.color('red')
        self.penup()
        self.speed(5)
        self.goto(x, y)
        self.direction = random.choice(['left', 'right'])

    def move(self, pipes):
        if self.direction == 'left':
            self.shape('cat_left.gif')
            dx = -22
            dy = 0

            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            if (move_to_x, move_to_y) not in pipes and (move_to_x, move_to_y - 22) in pipes \
                    and (move_to_x - 22, move_to_y) not in pipes:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(['left', 'right'])

        elif self.direction == 'right':
            self.shape('cat_right.gif')
            dx = +22
            dy = 0
            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            if (move_to_x, move_to_y) not in pipes and (move_to_x, move_to_y - 22) in pipes \
                    and (move_to_x + 22, move_to_y) not in pipes:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(['left', 'right'])

    def destroy(self):
        self.hideturtle()
