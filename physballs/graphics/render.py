import pygame
import time

display = pygame.display.set_mode((0, 0))
color = (0, 0, 0)
lineWidth = 1
circleWidth = 5
size = (0, 0)

def start(width, height, name, bgColor):
    global size
    size = (width, height)
    global color
    color = bgColor
    global display
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    display.fill(bgColor)
    pygame.display.flip()
def draw():
    pygame.display.flip()
    display.fill(color)

def addline(color, start_pos, end_pos):
    pygame.draw.line(display, color, (int(start_pos[0]), int(start_pos[1])), (int(end_pos[0]), int(end_pos[1])), lineWidth)

def setlinewidth(linewidth):
    global lineWidth
    lineWidth = linewidth

def addpoint(color, position):
    pygame.draw.circle(display, color, (int(position[0]), int(position[1])), circleWidth)
    
def setpointsize(pointSize):
    global circleWidth
    circleWidth = pointSize
def addlines(color, points):
    pygame.draw.lines(display, color, False, points, lineWidth)
