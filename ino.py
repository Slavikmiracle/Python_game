import pygame


class Ino(pygame.sprite.Sprite):
    "Создание инопланетянина"
    def __init__(self, screen):
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/Ino.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.x)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.05
        self.rect.y = self.y
