import pygame
import os

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "../images/ship.bmp")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
