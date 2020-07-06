import pygame
import time
import sys

(width, height) = (1200, 720)
screen = pygame.display.set_mode((width, height), 0, 32)
(midScreenX, midScreenY) = (width / 2, height / 2)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


def open_window():
    bg_color = (0, 0, 0)
    pygame.init()
    pygame.display.set_caption("Physballs")
    pygame.mouse.set_pos((midScreenX, midScreenY))
    loop(screen, bg_color)


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
        # Make the most recently drawn screen visible.

        pygame.display.flip()


# TODO in the future use pygame.font.get_init() to debug.

def display_text(text):
    text_font = pygame.font.SysFont("consolas", 14, False, False)
    pygame.font.Font.render(text, False, white, background=None)
