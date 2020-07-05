#!/usr/bin/env python3

import time

import pygame
import sys

(width, height) = (1200, 720)
screen = pygame.display.set_mode((width, height), 0, 32)
(midScreenX, midScreenY) = (width / 2, height / 2)


def open_window():
    bg_color = (0, 0, 0)
    pygame.init()
    pygame.display.set_caption("Physballs")
    pygame.mouse.set_pos((midScreenX, midScreenY))
    loop(screen, bg_color)


class Planet:

    # Size = Thickness obviously.
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 160, 153)
        self.thickness = 40

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)


def loop(a_screen, bg_color):
    last_time = time.time()
    # Game loop starts here.
    while True:

        # Get x, y coordinates of the pointer.
        print(pygame.mouse.get_pos())

        # Set up for frame independent physics
        delta_t = time.time() - last_time
        delta_t *= 60
        last_time = time.time()

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        a_screen.fill(bg_color)
        planet1 = Planet(50, 50, 40)
        planet1.display()

        # Make the most recently drawn screen visible.

        pygame.display.flip()


open_window()
