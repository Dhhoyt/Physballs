import pygame


def get_mouse_pos() -> tuple:
    while True:
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos
