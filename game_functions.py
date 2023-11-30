import sys

import pygame as pg


def check_event():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pg.display.flip()