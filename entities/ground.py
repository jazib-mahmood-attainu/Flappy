import pygame

from util.constants import Constants

class Ground:
    def __init__(self):
        self.image_source = "assets/images/ground.png"
        self.width = 37
        self.height = 128
        self.rnge = (Constants.width//self.width)+1 #21
        self.images = [pygame.image.load(self.image_source) for _ in range(self.rnge)]
        self.image_positions = []

    def get_position(self):
        positions = []
        dx = 0
        for i in range(self.rnge):
            x = self.width//2+dx
            y = Constants.height-self.height//2
            positions.append((x,y))
            dx += self.width
        return positions

    def display(self,screen):
        image_positions = self.get_position()
        for i in range(self.rnge):
            self.ground_rect = self.images[i].get_rect()
            self.ground_rect.center = image_positions[i]
            screen.blit(self.images[0],self.ground_rect)

