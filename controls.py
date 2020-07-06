import pygame


def get_mouse_pos():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos
