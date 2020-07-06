import pygame
from render import screen

planets = []

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


def create_planet(x_pos, y_pos, a_size):
    planets.append(Planet(x_pos, y_pos, a_size))


def create_planet():
    pass
