import pygame
import sys


def open_window():
    bg_color = (0, 0, 0)
    (width, height) = (1200, 720)
    pygame.init()
    pygame.display.set_caption("Physballs")
    screen = pygame.display.set_mode((width, height))

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
            print("test")

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


open_window()
