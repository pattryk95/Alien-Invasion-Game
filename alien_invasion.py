import pygame as pg
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_functions import check_events, update_screen, update_bullets


def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Inwacja Obcych")
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()

    while True:
        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        update_bullets(bullets)

        update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
