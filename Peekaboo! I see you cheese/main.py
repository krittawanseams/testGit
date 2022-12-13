import stage
import turtle
from turtle import Turtle
from mouse import Player
from stage import Stage
from stage import Pen

cheeses = []
enemies = []
nexts = []
maps = []
pipes = []
player_ = []
player = Player()
pen = Pen()
stage_ = Stage()

stage_.random_map(pen, player, pipes, player_)

window = turtle.Screen()
window.bgcolor("black")
window.title('Peekaboo! I see you cheese')
window.setup(700, 700)


def player_go_jump():
    player.go_jump(pipes, player)


def player_go_left():
    player.go_left(pipes, player)


def player_go_right():
    player.go_right(pipes, player)


def player_go_high_jump():
    player.go_highjump(pipes, player)


window.onkey(player_go_jump, "Up")
window.onkey(player_go_left, "Left")
window.onkey(player_go_right, "Right")
window.onkey(player_go_high_jump, "space")
window.listen()

pen_ = Turtle()
pen_.penup()
pen_.hideturtle()
pen_.setposition(180, 310)
pen_.hideturtle()
pen_.color('white')
pen_.width(30)

ask_howtoplay = input('Do you want to know how to play this game?(n/y) ')
if ask_howtoplay == 'y':
    print('How to play:\n'
          'Use the arrow keys to move the mouse\n'
          '(Up arrow --> jump\n'
          'Left arrow --> walk to the left\n'
          'Right arrow --> walk to the right) \n'
          'and Use the space bar to high jump\n'
          ', and the pink circle in map is the door to next map')
    print()
ask_warning = input('Do you want to know about the warning in this game?(n/y) ')
if ask_warning == 'y':
    print("!! You cannot jump if there is no space above the mouse's head, and you cannot \n"
          "high jump if there is less than 4 squares above the mouse's head, and if you \n"
          "get caught by cat, it's game over!!")
    print()

ask_ready = input('Are you ready??(n/y) ')
if ask_ready == 'y':
    print("Let's start!")
    stage.loop_stage(player, pipes, pen_, window, player_)
    window.bgcolor("black")
    pen_.clear()
    pen_.penup()
    pen_.setposition(-100, -100)
    pen_.hideturtle()
    pen_.write(f'Total Cheese : {player.cheese}', font=('Arial', 20, 'normal'))
    print(f'Total Cheese : {player.cheese}')
    print(f'Thank you :)')
    cont_play = input('Do you want to continue?(n/y) ')
    while cont_play != 'n':
        if cont_play == 'y':
            pen_.clear()
            player = Player()
            window = turtle.Screen()
            window.bgcolor("black")
            window.title('Peekaboo! I see you cheese')
            window.setup(700, 700)
            window.onkey(player_go_jump, "Up")
            window.onkey(player_go_left, "Left")
            window.onkey(player_go_right, "Right")
            window.onkey(player_go_high_jump, "space")
            window.listen()
            game_stage = Stage()
            game_stage.random_map(pen, player, pipes, player_)
            stage.loop_stage(player, pipes, pen_, window, player_)
        cont_play = input('Do you want to continue?(n/y) ')
else:
    print(f'Thank you :)')
