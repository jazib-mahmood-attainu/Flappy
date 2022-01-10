import pygame
from entities.sprite import Sprite

from util.constants import Constants

class Ground(Sprite):
    def __init__(self):
        self.image_source = "assets/images/ground.png"
        self.image = pygame.image.load(self.image_source)
        self.width = 37
        self.height = 128
        self.sprites = 2*((Constants.width//self.width)+1)
        self.images = [self.image.get_rect() for _ in range(self.sprites)]
        self.positions = []
        self.draw_platform()

    def draw_platform(self):
        dx = 0
        for i in range(self.sprites):
            x = self.width//2+dx
            y = Constants.height-self.height//2

            self.positions.append((x,y))
            dx += self.width

    def update_platform(self):
        speed = 0.4
        for idx in range(len(self.positions)):
            x,y = self.positions[idx]
            if x <=-1*Constants.width:
                self.positions[idx] = (Constants.width+self.width//2,y)
            else:
                self.positions[idx] = (x-speed,y)#future im going to add speed here




    def display(self,screen):
        self.update_platform()
        for i in range(self.sprites):
            ground_rect = self.images[i]
            ground_rect.center = self.positions[i]
            screen.blit(self.image,ground_rect)

