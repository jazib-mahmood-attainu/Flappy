import sys, pygame
from entities.background import Background
from entities.bird import Bird
from entities.ground import Ground
from util.constants import Constants
from util.colors import Colors

def run():
    pygame.init()
    screen = pygame.display.set_mode((Constants.width,Constants.height))
    background = Background()
    bird = Bird()
    ground = Ground()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        background.display(screen)
        bird.display(screen)
        ground.display(screen)
    

        pygame.display.flip()

if __name__=="__main__":
    run()