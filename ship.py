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

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):

        self.screen.blit(self.image, self.rect)
