import pygame as pg
import numpy as np
import keyboard as key
import random

pg.init()

size = (1040, 1040)
screen = pg.display.set_mode(size)
pg.display.set_caption('Ray Casting Test')

# variables
rot = 0

pos_x, pos_y = (size[0]/2, size[1]/2)

obj1_x, obj1_y = (pos_x + np.cos(random.randrange(10)) * random.randrange(500),
                  pos_y + np.sin(random.randrange(10)) * random.randrange(500))

circleRect = pg.rect.Rect((obj1_x, obj1_y), (30, 30))

# configurable variables

line_count = 15

rot_move = 0.05

fov = 60

per_rot = 0

# main game loop

line_rot_move = (fov * 2) / line_count / 100

while True:

    screen.fill((0, 0, 0))
    runs = 0

    for i in range(1, line_count + 2):
        if line_count % 2 == 0:
            line_rot = rot - ((line_count / 2) / 100) + per_rot

        else:
            line_rot = rot - (((line_count-1) / 2) / 100) + per_rot

        if runs > 0:
            per_rot += line_rot_move

        pg.draw.circle(screen, (0, 255, 0), (obj1_x + 15, obj1_y + 15), 15)

        runs += 1

        for dist in range(500):

            distance = dist

            sin, cos = (np.sin(line_rot),
                        np.cos(line_rot))

            check_x, check_y = (pos_x + cos * dist,
                                pos_y + sin * dist)

            if circleRect.collidepoint(check_x, check_y):
                distance = dist
                dist_x, dist_y = (pos_x + cos * distance,
                                  pos_y + sin * distance)

                print(f'{i}: dist: {distance}\n')

                pg.draw.line(screen, (255, 0, 0), (pos_x, pos_y), (dist_x, dist_y), 5)

            elif not circleRect.collidepoint(check_x, check_y):

                dist_x, dist_y = (check_x, check_y)

                pg.draw.line(screen, (0, 0, 255), (pos_x, pos_y), (dist_x, dist_y), 1)
    per_rot = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    while True:
        try:
            if key.is_pressed('d'):
                rot += rot_move
                break

            if key.is_pressed('a'):
                rot -= rot_move
                break

            if key.is_pressed('space'):
                obj1_x, obj1_y = (pos_x + np.cos(random.randrange(10)) * random.randrange(500),
                                  pos_y + np.sin(random.randrange(10)) * random.randrange(500))
                circleRect = pg.rect.Rect((obj1_x, obj1_y), (30, 30))

                break

            if key.is_pressed('escape'):
                pg.quit()
                break

        except:
            break
        break

    print(f'rot:  {rot}\n')
    pg.display.flip()

