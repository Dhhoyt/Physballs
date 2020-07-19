import pygame
import time
import controls
import planets

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
        controls.check_event(running)

        # Update game elements.

        planets.iterate_planets()

        # Fill canvas
        a_screen.fill(bg_color)

        # Draw surfaces.

        # Update surface.
        pygame.display.flip()

    pygame.quit()


# TODO implement MORE DEBUGGING AAA


def display_text(text, a_screen, bg_color):
    a_screen.fill(bg_color)
    text_font = pygame.font.SysFont("consolas", 14)
    text_surface = text_font.render(text, False, (0, 255, 0))
    screen.blit(text_surface, (10, 10))