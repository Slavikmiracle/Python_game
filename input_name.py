import pygame
from pygame.sprite import Sprite


class Input_name(Sprite):
    "Выводит окно ввода имени"
    def __init__(self, screen):
        super(Input_name, self).__init__()
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.color_font = 139, 195, 74
        self.text_name_image = self.font.render("Enter name  ", True,
                                      self.color_font, (0, 0, 0))
        self.text_name_rect = self.text_name_image.get_rect()
        self.text_name_rect.centerx = 170
        self.text_name_rect.top = 60
        self.input_box = pygame.Rect(100, 100, 140, 32)
        self.active = False
        self.text = ''
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        self.active = not self.active
                    else:
                        self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            self.done = True
                            self.name_input = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode

            screen.fill((0, 0, 0))
            self.txt_surface = self.font.render(self.text, True,  self.color)
            width = max(200, self.txt_surface.get_width()+10)
            self.input_box.w = width
            screen.blit(self.text_name_image, self.text_name_rect)
            screen.blit(self.txt_surface, (self.input_box.x+5,  self.input_box.y+5))
            pygame.draw.rect(screen,  self.color,  self.input_box, 2)
            pygame.display.flip()

