from pygame import image
from entities.sprite import Sprite
from util.constants import Constants
import pygame
import random

class Pipe(Sprite):
    def __init__(self):
        self.width = Constants.pipe_width
        self.height = Constants.pipe_height
        self.image_source = "assets/images/pipe.png"
        self.image = pygame.image.load(self.image_source)
        self.pipes = []

    def spawn_pipe(self):
        rect_bottom = self.image.get_rect()
        # rn_bottom = 0#random.randint(10,200)

        # rect_bottom.midbottom = (
        #     Constants.width + self.width,Constants.height+self.height//2 + rn_bottom
        # )

        # rn_top = Constants.height-rn_bottom#random.randint()
        # rect_top = self.image.get_rect()
        # rect_top.midtop = (
        #  Constants.width + self.width,self.height//2+rn_top   
        # )

        self.pipes.append(rect_bottom)
        # self.pipes.append(rect_top)
    
    # def move_pipe(self):
    #     for pipe in self.pipes:
    #         pipe.centerx -=2

    def display(self,screen):
        # self.spawn_pipe()
        # for pipe in self.pipes:
        #     # if pipe.midtop[1]<0:
        #     #     screen.blit(pygame.transform.rotate(self.image,180),pipe)
        #     # else:
        #     screen.blit(self.image,pipe)
        screen.blit(self.image,self.image.get_rect())
