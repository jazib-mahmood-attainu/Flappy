# from os import pipe
from entities.pipes import Pipe
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
    pipe = Pipe()
    
    SPAWN_PIPE_EVENT = pygame.USEREVENT+1

    # pygame.time.set_timer(pygame.USEREVENT,200)
    # pygame.time.set_timer(SPAWN_PIPE_EVENT,1500)

    ctr = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird.jump()
                if event.type == pygame.USEREVENT:
                    bird.animate()
                # if event.type == SPAWN_PIPE_EVENT:
                #     pipe.spawn_pipe()
        # pipe.spawn_pipe()
        bird.apply_gravity()
        # pipe.move_pipe()
        pipe.display(screen)
        background.display(screen)
        bird.display(screen)
        ground.display(screen)
        ctr+=1
        print(ctr)
        pygame.display.flip()

if __name__=="__main__":
    run()