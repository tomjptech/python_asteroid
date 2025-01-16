# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    asteroids_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for update_obj in updatable:
            update_obj.update(dt)

        screen.fill([0,0,0])

        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        pygame.display.flip()

        dt = asteroids_clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()