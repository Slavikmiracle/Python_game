import pygame
from pygame.sprite import Sprite

class Menu(Sprite):
    "Вывод окна меню"
    def __init__(self, screen):
        super(Menu, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/start.png').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = (700 / 2, 700 / 2)
        self.image1 = pygame.image.load('image/exit.png').convert()
        self.rect1 = self.image1.get_rect()
        self.screen_rect1 = screen.get_rect()
        self.rect1.center = (700 / 2, 700 / 2 + 200)
        self.click = False

    def output(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image1, self.rect1)
