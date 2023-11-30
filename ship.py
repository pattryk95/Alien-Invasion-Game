import pygame as pg


class Ship:

    def __init__(self, screen):
        self.screen = screen

        self.image = pg.image.load('images/spaceship.bmp')
        self.image = pg.transform.scale(self.image, (75, 150))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)
