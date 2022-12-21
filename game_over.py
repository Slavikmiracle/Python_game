import pygame
from pygame.sprite import Sprite

class Game_over(Sprite):
    "Выводит картинку Game Over"
    def __init__(self, screen):
        super(Game_over, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/Game_over.png').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = (700 / 2, 700 / 2)

    def output(self):
        self.screen.blit(self.image, self.rect)
