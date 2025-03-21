# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #player location
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

    #to track time
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
    
    
if __name__ == "__main__":
    main()