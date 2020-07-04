import pygame
import time
import pygame
import sys


def apply_force():
    pass


def open_window():
    bg_color = (0, 0, 0)
    (width, height) = (1200, 720)
    pygame.init()
    pygame.display.set_caption("Physballs")
    screen = pygame.display.set_mode((width, height))
    fps = pygame.time.Clock()

    class Planet:

        # Size = Thickness obviously.
        def __init__(self, x, y, size):
            self.x = x
            self.y = y
            self.size = size
            self.color = (255, 160, 153)
            self.thickness = 40

        def move(self, x, y):
            pass

        def display(self):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        planet1 = Planet(50, 50, 40)
        planet1.display()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

        # Frame independent physics, scrapped until further testing.
        """prev_time = time.time()
        pygame.display.update()
        delta = time.time() - prev_time
        move_distance = delta * 64  # Would move 64 pixels per second because delta is a fraction of a second
        prev_time = time.time()
        """


open_window()
