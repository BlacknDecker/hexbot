import json
import math

import pygame
import sys
import requests

from pygame.constants import QUIT
from pprint import pprint

BASE_URL = "https://api.noopschallenge.com/hexbot"
SURFACE_DIMENSION = 500
SQUARE_N = 50
SQUARE_DIMENSION = math.floor(SURFACE_DIMENSION/SQUARE_N)
WHITE = (255, 255, 255)     # set up the bg color


def setup():
    global DISPLAYSURF
    pygame.init()
    # set up the window
    DISPLAYSURF = pygame.display.set_mode((SURFACE_DIMENSION, SURFACE_DIMENSION), 0, 32)
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
        _set_surface_colors(SURFACE_DIMENSION-SQUARE_DIMENSION, SURFACE_DIMENSION-SQUARE_DIMENSION)   # Set  random color
        pygame.display.update()


def _set_surface_colors(w_width, w_height):
    # Get Random Colors
    reply = requests.get(BASE_URL, params={"count": 1000,
                                           "width": w_width,
                                           "height": w_height})
    # Get surface pixels:
    pix_surf = pygame.PixelArray(DISPLAYSURF)
    # Assign colors to pixels
    colors = reply.json()["colors"]     # List of color + coordinates
    for col in colors:
        coo_x = col["coordinates"]["x"]
        coo_y = col["coordinates"]["y"]
        pix_surf[coo_x:coo_x+SQUARE_DIMENSION, coo_y:coo_y+SQUARE_DIMENSION] = pygame.Color(col["value"])


setup()
loop()
