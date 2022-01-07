import pygame

class Background:
    def __init__(self):
        self.image_source = "assets/images/background.png"
        self.bg = pygame.image.load(self.image_source)

    def display(self,screen):
        self.bg_rect = self.bg.get_rect()
        screen.blit(self.bg,self.bg_rect)

