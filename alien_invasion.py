import pygame as pg
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen


def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Inwacja Obcych")
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:
        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        update_screen(ai_settings, screen, ship, bullets)


run_game()
