import pygame as pg

from settings import Settings
from ship import Ship
from game_functions import check_event, update_screen


def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Inwacja Obcych")
    ship = Ship(ai_settings, screen)

    while True:
        check_event(ship)
        ship.update()
        update_screen(ai_settings, screen, ship)


run_game()
