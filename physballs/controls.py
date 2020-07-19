import pygame
import sys
import render
import planets


# TODO make it so when a player clicks a planet is created in that position


def check_event(running):
    for event in pygame.event.get():

        # Check for mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("click")
                planets.create_planet((73, 78), 40)

        if event.type == pygame.QUIT:
            running = False

            sys.exit()


def is_mouse_held():
    if pygame.mouse.get_pressed()[0]:
        pass


def get_mouse_pos() -> tuple:
    mouse_pos = pygame.mouse.get_pos()
    return mouse_pos
