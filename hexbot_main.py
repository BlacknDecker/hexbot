import json

import pygame
import sys
import requests

from pygame.constants import QUIT
from pprint import pprint

BASE_URL = "https://api.noopschallenge.com/hexbot"
SURFACE_DIMENSIONS = (500, 500)
WHITE = (255, 255, 255)     # set up the bg color


def setup():
    global DISPLAYSURF
    pygame.init()
    # set up the window
    DISPLAYSURF = pygame.display.set_mode(SURFACE_DIMENSIONS, 0, 32)
    pygame.display.set_caption('Hexbot')


def loop():
    # draw on the surface object
    DISPLAYSURF.fill(WHITE)
    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        _set_surface_colors(SURFACE_DIMENSIONS[0], SURFACE_DIMENSIONS[1])   # Set  random color
        pygame.display.update()


def _set_surface_colors(w_width, w_height):
    # Get Random Colors
    reply = requests.get(BASE_URL, params={"count": 1000,
                                           "width": w_width,
                                           "height": w_height,
                                           "seed": "FF7F50,FFD700,FF8C00"})
    # Get surface pixels:
    pix_surf = pygame.PixelArray(DISPLAYSURF)
    # Assign colors to pixels
    colors = reply.json()["colors"]     # List of color + coordinates
    for col in colors:
        pix_surf[col["coordinates"]["x"], col["coordinates"]["y"]] = pygame.Color(col["value"])


setup()
loop()
