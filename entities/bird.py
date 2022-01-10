import pygame
from entities.sprite import Sprite

from util.constants import Constants

class Bird(Sprite):
    bird_frame = 0
    def __init__(self):
        self.image_source = "assets/images/bird.png"
        self.bird = pygame.image.load(self.image_source)
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.center = (400,200)
        self.acceleration = 0
    
    def jump(self):
        self.acceleration -= 2

    def apply_gravity(self):
        gravity = 0.0025
        self.acceleration += gravity
    
    def animate(self):
        Bird.bird_frame = (Bird.bird_frame+1)%3

    def display(self,screen):
        self.bird_rect.centery += self.acceleration
        screen.blit(self.bird,self.bird_rect,(Bird.bird_frame * Constants.bird_width,0,Constants.bird_width,Constants.bird_height))

