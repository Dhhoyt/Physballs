import pygame
import time
from game.loop import loop

(width, height) = (1200, 720)
(midScreenX, midScreenY) = (width / 2, height / 2)
screen = pygame.display.set_mode((width, height), 0, 32)
color = (0, 0, 0)
lineWidth = 1
circleWidth = 5
size = (0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


def add_line(line_color, start_pos, end_pos):
    pygame.draw.line(screen, line_color, (int(start_pos[0]), int(start_pos[1])), (int(end_pos[0]), int(end_pos[1])),
                     lineWidth)


def set_line_width(line_width):
    global lineWidth
    lineWidth = line_width


def add_point(point_color, position):
    pygame.draw.circle(screen, point_color, (int(position[0]), int(position[1])), circleWidth)


def set_point_size(point_size):
    global circleWidth
    circleWidth = point_size


def add_lines(lines_color, points):
    pygame.draw.lines(screen, lines_color, False, points, lineWidth)


def open_window():
    bg_color = (0, 0, 0)
    pygame.init()
    pygame.display.set_caption("Physballs")
    pygame.mouse.set_pos((midScreenX, midScreenY))
    loop(screen, bg_color, True)


def display_text(text, a_screen, bg_color):
    a_screen.fill(bg_color)
    text_font = pygame.font.SysFont("consolas", 14)
    text_surface = text_font.render(text, False, (0, 255, 0))
    screen.blit(text_surface, (10, 10))
