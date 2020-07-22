import math
import random
import schedule
from ball import Ball
from ball import *
from graphics import render

speed = 1
g_const = 1
step = 0


def calc_force(ball1, ball2):
    before_force = g_const * ball1.size * ball2.size
    x_dist = ball2.pos[0] - ball1.pos[0]
    y_dist = ball2.pos[1] - ball1.pos[1]
    dist = math.pow(x_dist, 2) + math.pow(y_dist, 2)
    if math.sqrt(dist) < ball1.radius + ball2.radius:
        # New x velocity.
        new_xv = ((ball1.velocity[0] * ball1.size) + (ball2.velocity[0] * ball2.size)) / (ball1.size + ball2.size)
        # New y velocity.
        new_yv = ((ball1.velocity[1] * ball1.size) + (ball2.velocity[1] * ball2.size)) / (ball1.size + ball2.size)
        # New x pos.
        new_xp = (ball1.pos[0] + ball2.pos[0]) / 2
        # New y pos.
        new_yp = (ball1.pos[1] + ball2.pos[1]) / 2

        add_ball((new_xp, new_yp), ball1.size + ball2.size, (new_xv, new_yv), (255, 255, 255))
        if ball1 in Ball.balls:
            Ball.balls.remove(ball1)
        if ball2 in Ball.balls:
            Ball.balls.remove(ball2)
        return 0, 0
    force = (before_force / dist)
    if x_dist == 0:
        theta = math.pi / 2
    else:
        theta = math.atan(y_dist / x_dist)
    if x_dist == 0:
        x_force = 0
    else:
        x_force = math.fabs(force * math.cos(theta)) * (x_dist / math.fabs(x_dist))
    if y_dist == 0:
        y_force = 0
    else:
        y_force = math.fabs(force * math.sin(theta)) * (y_dist / math.fabs(y_dist))
    return x_force, y_force


# This function is for debugging purposes.

def random_balls():
    for i in range(5):
        vel = (random.random() - 0.5, random.random() - 0.5)
        pos = (random.randint(0, render.width), random.randint(0, render.height))
        rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        add_ball(pos, random.randint(3, 50), vel, rand_color)


def calc_pos():
    for ball in Ball.balls:
        x_vel = ball.velocity[0]
        y_vel = ball.velocity[1]
        for j in Ball.balls:
            if ball == j:
                continue

            force = calc_force(ball, j)
            x_vel += (force[0] / ball.size)
            y_vel += (force[1] / ball.size)

        x_pos = (ball.pos[0] + x_vel)

        if x_pos < 0:
            x_pos = 1
            x_vel = 0
        if x_pos > render.size[0]:
            x_pos = render.size[0] - 1
            x_vel = 0
        y_pos = (ball.pos[1] + y_vel)
        if y_pos < 0:
            y_pos = 1
            y_vel = 0
        if y_pos > render.size[1]:
            y_pos = render.size[1] - 1
            y_vel = 0

        ball.future_pos = (x_pos, y_pos)
        ball.velocity = (x_vel, y_vel)
        render.set_point_size(ball.radius)
        render.add_point(ball.color, ball.pos)

    for ball in Ball.balls:
        ball.pos = ball.future_pos
