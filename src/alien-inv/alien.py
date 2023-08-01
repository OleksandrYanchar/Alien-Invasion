import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        # Initialize alien and sets it starter position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # stare each new alien and set its rect attribute
        self.image = pygame.image.load("../images/alien.bmp")
        self.rect = self.image.get_rect()

        # start each alien near the top left of the map
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horisontal position
        self.x = float(self.rect.x)

    def update(self):
        # move aliens to the right
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        # returning True if alien is in edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
