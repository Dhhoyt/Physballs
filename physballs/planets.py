import pygame
import render
import controls
from render import *
planets_arr = []


class Planet:

    # Size = Thiccness obviously.
    def __init__(self, pos: tuple, size):
        self.pos = pos
        self.size = size
        self.color = (255, 160, 153)
        self.thickness = size

    def display(self):
        pygame.draw.circle(render.screen, self.color, self.pos, self.size, self.thickness)


def create_planet(pos: tuple, a_size):
    if controls.is_mouse_held():
        planets_arr.append(Planet(pos, a_size))


def iterate_planets():
    for planet in planets_arr:
        print(str(planets_arr[planet].create_planet(midScreenX, midScreenY, 40)))
