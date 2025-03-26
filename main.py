# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    #to track time
    clock = pygame.time.Clock()

    #creating group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #automaticaly adds player instance to updatable and drawable groups
    Player.containers = (updatable , drawable)

    #set instances for asteroids
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    #create instance of asteroids and players
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #check for collision
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("game over!!")
                return #exit the game

        #make the screen
        screen.fill("black", rect=None, special_flags=0)

        #draw the objects in the game
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
    
    
if __name__ == "__main__":
    main()

    