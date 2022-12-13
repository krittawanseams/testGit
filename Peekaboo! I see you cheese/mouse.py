import math
import turtle
from turtle import Turtle

window = turtle.Screen()
window.bgcolor("black")
window.setup(700,700)

# turtle.register_shape("bg.gif")
# turtle.register_shape("cat_left.gif")
# turtle.register_shape("cat_right.gif")
turtle.register_shape("mouse_left.gif")
turtle.register_shape("mouse_right.gif")
# turtle.register_shape("cheese2.gif")
# turtle.register_shape("pipe_hori.gif")
# turtle.register_shape("pipe_venti.gif")

# total_player_cheese + player.cheese

class Pen(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('pipe_hori.gif')
        self.color('white')
        self.penup()
        self.speed(0)

# class Pen2(Turtle):
#     def __init__(self):
#         Turtle.__init__(self)
#         self.shape('pipe_venti.gif')
#         self.color('white')
#         self.penup()

#         self.speed(0)

class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('mouse_right.gif')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.cheese = 0
        # self.goto(x,y)

    def go_jump(self,pipes,player):
        self.speed(3)
        if self.heading() == 0:
            move_to_x = player.xcor() + 22
            move_to_y = player.ycor() + 22
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes:
                self.goto(move_to_x, move_to_y)
        if self.heading() == 180:
            move_to_x = player.xcor() - 22
            move_to_y = player.ycor() + 22
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes:
                self.goto(move_to_x, move_to_y)
        while (self.xcor(), self.ycor() - 22) not in pipes:
            self.goto(self.xcor(), self.ycor() - 22)
        self.speed(3)

    def go_highjump(self,pipes,player):
        self.speed(3)
        if self.heading() == 0:
            move_to_x = player.xcor() + 22
            move_to_y = player.ycor() + 66
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes and (self.xcor(), self.ycor() + 44) not in pipes and (self.xcor(), self.ycor() + 66) not in pipes:
                self.goto(move_to_x, move_to_y)
        self.speed(3)
        if self.heading() == 180:
            move_to_x = player.xcor() - 22
            move_to_y = player.ycor() + 66
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes and (self.xcor(), self.ycor() + 44) not in pipes and (self.xcor(), self.ycor() + 66) not in pipes:
                self.goto(move_to_x, move_to_y)
        while (self.xcor(), self.ycor() - 22) not in pipes :
            self.goto(self.xcor(), self.ycor() - 22)
        self.speed(3)


    def go_left(self,pipes,player):
        self.shape('mouse_left.gif')
        move_to_x = player.xcor() - 22
        move_to_y = player.ycor()
        self.setheading(180)
        if (move_to_x, move_to_y) not in pipes:
            self.goto(move_to_x, move_to_y)
            if (move_to_x, move_to_y - 22) not in pipes:
                self.goto(move_to_x, move_to_y)
        while True:
            if (self.xcor(), self.ycor() - 22) not in pipes:
                self.goto(player.xcor(), self.ycor()-22)
            else:
                break

    def go_right(self,pipes,player):
        self.shape('mouse_right.gif')
        move_to_x = player.xcor() + 22
        move_to_y = player.ycor()
        self.setheading(0)
        if (move_to_x, move_to_y) not in pipes and (move_to_x  , move_to_y - 22) in pipes:
            self.goto(move_to_x, move_to_y)
        elif (move_to_x, move_to_y) not in pipes and (move_to_x, move_to_y - 22) not in pipes:
            self.goto(move_to_x, move_to_y - 22)
        while True:
            if (self.xcor(), self.ycor() - 22) not in pipes:
                self.goto(player.xcor(), self.ycor()-22)
            else:
                break

    def is_collision(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()

# player = Player()
# import math
# class Window(TurtleScreen):
#     def __init__(self):
#         TurtleScreen.__init__(self)
#         # window = TurtleScreen()
#         # window.bgcolor("black")
#         # window.setup(700,700)
#         # print(window)
#         self.bgcolor("black")
#         self.setup(700,700)

# import turtle
# from turtle import Turtle
# window = turtle.Screen()
# window.bgcolor("black")
# # window.bgpic("bg.gif")
# window.setup(700,700)
# # window.onkey(player.go_jump,"Up")
# # window.onkey(player.go_left,"Left")
# # window.onkey(player.go_right,"Right")
# # window.onkey(player.go_longjump,"space")
# window.listen()
# def window(player):
#     window.onkey(player.go_jump, "Up")
#     window.onkey(player.go_left, "Left")
#     window.onkey(player.go_right, "Right")
#     window.onkey(player.go_longjump, "space")
# window()