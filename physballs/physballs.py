from graphics import render
import ball
import math
import time
import schedule
import random
render.start(1000, 1000, "Physballs", (0,0,0))
balls = []
speed = 1
gravconst = 1
running = True
step = 0
def addball(pos: tuple, size, velocity: tuple, color):
    nuvelocity = (velocity[0] , velocity[1])
    balls.append(ball.ball(pos, size, nuvelocity, int(size**(1)), color))
    print(pos)
def calcforce(ball1, ball2):
    beforeforce = gravconst * ball1.size * ball2.size
    xdist = ball2.pos[0] - ball1.pos[0]
    ydist = ball2.pos[1] - ball1.pos[1]
    dist = math.pow(xdist, 2) + math.pow(ydist, 2)
    if math.sqrt(dist) < ball1.radius + ball2.radius:
        newxv = ((ball1.velocity[0] * ball1.size) + (ball2.velocity[0] * ball2.size))/(ball1.size + ball2.size)
        newyv = ((ball1.velocity[1] * ball1.size) + (ball2.velocity[1] * ball2.size))/(ball1.size + ball2.size)
        newxp = (ball1.pos[0]  + ball2.pos[0])/2
        newyp = (ball1.pos[1]  + ball2.pos[1])/2
        print(newxp, newyp)
        print(newxv, newyv)
        addball((newxp, newyp), ball1.size + ball2.size, (newxv, newyv),  (255,255,255))
        if ball1 in balls:
            balls.remove(ball1)
        if ball2 in balls:
            balls.remove(ball2)
        return (0, 0)
    force = (beforeforce / dist)
    if xdist ==  0:
        theta = math.pi/2
    else:
        theta = math.atan(ydist/xdist)
    if xdist == 0:
        xforce = 0
    else:
        xforce = math.fabs(force*math.cos(theta)) * (xdist/math.fabs(xdist))
    if ydist == 0:
        yforce = 0
    else:
        yforce = math.fabs(force*math.sin(theta)) * (ydist/math.fabs(ydist))
    return (xforce, yforce)

for i in range(5):
    vel  = (random.random() - 0.5,random.random() - 0.5)
    pos = (random.randint(0, render.size[0]), random.randint(0, render.size[1]))
    randcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    addball(pos , random.randint(3, 50), vel, randcolor)

def calcpos():
    for i in balls:
        if not i in balls:
            print("g")
            continue
        xvel = i.velocity[0]
        yvel = i.velocity[1]
        for j in balls:
            if i == j:
                continue
            force = calcforce(i , j)
            xvel += (force[0]/i.size)
            yvel += (force[1]/i.size)
        xpos = (i.pos[0] + xvel)
        ypos = (i.pos[1] + yvel)
        if xpos < 0:
            print(xpos)
            print("here")
            xpos = 1
            xvel = 0
        if xpos > render.size[0]:
            print(xpos)
            print("here")
            xpos = render.size[0] - 1
            xvel = 0
        ypos = (i.pos[1] + yvel)
        if ypos < 0:
            print(ypos)
            print("here")
            ypos = 1
            yvel = 0
        if ypos > render.size[1]:
            print(ypos)
            print("here")
            ypos = render.size[1] - 1
            yvel = 0
        i.futurepos = (xpos, ypos)
        i.velocity = (xvel, yvel)
        render.setpointsize(i.radius)
        render.addpoint(i.color, i.pos)
    render.draw()
    for i in balls:
        i.pos = i.futurepos
        
schedule.every(0.001).seconds.do(calcpos)
while True:
   schedule.run_pending()