import pygame
import time
import sys
import controls

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
    loop(screen, bg_color, True)


def loop(a_screen, bg_color, running):
    last_time = time.time()
    # Game loop starts here.
    while running:

        # Set up for frame independent physics
        delta_t = time.time() - last_time
        delta_t *= 60
        last_time = time.time()

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False  # Be IDLE friendly
                sys.exit()

        a_screen.fill(bg_color)
        # Make the most recently drawn screen visible.
        display_text("Pointer coordinates: " + str(controls.get_mouse_pos()), a_screen, bg_color)
        pygame.display.flip()

    pygame.quit()


# TODO in the future use pygame.font.get_init() to debug.

def display_text(text, a_screen, bg_color):
    a_screen.fill(bg_color)
    text_font = pygame.font.SysFont("consolas", 14)
    text_surface = text_font.render(text, False, (0, 255, 0))
    screen.blit(text_surface, (10, 10))
