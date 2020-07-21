import time
import pygame
import controls
import sys
from graphics.render import display_text


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

        #fill
        a_screen.fill(bg_color)
        #draw
        display_text("Pointer coordinates: " + str(controls.get_mouse_pos()), a_screen, bg_color)
        #display
        pygame.display.flip()

    pygame.quit()