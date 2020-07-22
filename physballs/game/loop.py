import time
import pygame
from physics import gravity
import controls
import schedule
import sys

schedule.every(0.001).seconds.do(gravity.calc_pos)


def loop(a_screen, bg_color, running):
    last_time = time.time()
    # Game loop starts here.

    gravity.random_balls()

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

        # fill
        a_screen.fill(bg_color)
        # draw
        schedule.run_pending()
        # display
        pygame.display.flip()

    pygame.quit()
