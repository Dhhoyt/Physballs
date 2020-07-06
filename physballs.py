#!/usr/bin/env python3

import time
import pygame
import sys

from render import open_window

# TODO instead of creating objects within your game loop,
# create them once somewhere else and store
# them in an array somewhere. then, inside
# your game loop, iterate through the array of all game objects and call display() on them
# this will also allow you to create (and destroy) game objects without having to touch your game loop logic
from render import open_window

open_window()
