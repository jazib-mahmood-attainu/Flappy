import pygame

from util.constants import Constants

class Bird:
    def __init__(self):
        self.image_source = "assets/images/bird.png"
        self.bird = pygame.image.load(self.image_source)
        self.count = 0

    def display(self,screen):
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.center = Constants.width//2,Constants.height//2
        screen.blit(self.bird,self.bird_rect)

