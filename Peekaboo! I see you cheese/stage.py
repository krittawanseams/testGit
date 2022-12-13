import turtle
from turtle import Turtle
import json
import random
from cheese import Cheese
from cat import Enemy
from next_level import NextLevel

turtle.register_shape("pipe_hori.gif")
turtle.register_shape("cheese2.gif")
turtle.register_shape("cat_left.gif")
turtle.register_shape("cat_right.gif")


# to make a pipe-shaped map
class Pen(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('pipe_hori.gif')
        self.color('white')
        self.penup()
        self.speed(0)


class Stage:
    def __init__(self):
        self.cheese = 0
        self.name = ''
        self.next_map = ''

    # random map from maps.json
    def random_map(self, pen, player, pipes, player_):

        # read json file
        try:
            with open('maps.json', 'r') as f:
                all_maps = json.load(f)
        except FileNotFoundError:
            pass
        else:
            random_map = random.choice(list(all_maps.values()))

            # loop to read a map
            for y in range(len(random_map)):
                for x in range(len(random_map[y])):
                    character = random_map[y][x]
                    screen_x = -286 + (x * 22)
                    screen_y = 286 - (y * 22)
                    if character == 'X':
                        pen.goto(screen_x, screen_y)
                        pen.stamp()
                        pipes.append((screen_x, screen_y))
                    elif character == 'P':
                        player_.append(player.goto(screen_x, screen_y))
                    elif character == 'C':
                        cheeses.append(Cheese(screen_x, screen_y))
                    elif character == 'E':
                        enemies.append(Enemy(screen_x, screen_y))
                    elif character == 'N':
                        nexts.append(NextLevel(screen_x, screen_y))


cheeses = []
enemies = []
nexts = []


def loop_stage(player, pipes, pen_, window, player_):
    sum = 0
    while True:
        # when the mouse catches the cheese, the score is calculated and the cheese disappear.
        for cheese in cheeses:
            if player.is_collision(cheese):
                player.cheese += cheese.cheese
                print('Player Cheese: {}'.format(player.cheese))
                pen_.clear()
                pen_.penup()
                pen_.write(f'Cheese : {player.cheese}', font=('Arial', 20, 'normal'))
                cheese.destroy()
                cheeses.remove(cheese)
        # when the mouse catches the pink circle, it will remove to the next map.
        for next in nexts:
            if player.is_collision(next):
                next.destroy()
                nexts.remove(next)
                window.clear()
                pipes.clear()
                enemies.clear()
                pen_.clear()
                player_.clear()
                return player.cheese
        # the cat will take a walk. If the cat catches the mouse, it's game over.
        sum += 1
        if sum % 5 == 0:
            for enemy in enemies:
                enemy.move(pipes)
                if player.is_collision(enemy):
                    print('GAME OVER!! You have been caught by the cat')
                    player.destroy()
                    window.clear()
                    window.bgcolor("black")
                    pen_.clear()
                    pen_.penup()
                    pen_.setposition(-100, -100)
                    pen_.hideturtle()
                    pen_.write(f'Total Cheese : {player.cheese}', font=('Arial', 20, 'normal'))
                    print(f'Total Cheese : {player.cheese}')
                    print(f'Thank you :)')
                    return player.cheese
        window.update()
