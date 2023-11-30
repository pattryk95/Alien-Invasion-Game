import sys

import pygame as pg


def check_event(ship):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pg.display.flip()