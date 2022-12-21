import pygame.font

import controls
from gun import Gun
from pygame.sprite import Group

class Scores():
    def __init__(self, screen, stats, text_input, cur):
        self.cur = cur
        self.text_input = text_input
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        "Показывает текущий результат"
        self.score_img = self.font.render(self.text_input.text + " - " + str(self.stats.score),
                                          True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.screen_rect.top = 20

    def image_high_score(self):
        "Показывает лучший результат"
        self.high_score_image = self.font.render("Лучший результат - "+str(controls.score_database(self.cur)), True,
                                                 self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top + 30

    def image_guns(self):
        "Показывает сколько жизней осталось"
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        "Отрисовывает текущий и лучший результат"
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)