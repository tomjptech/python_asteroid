# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    asteroids_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for update_obj in updatable:
            update_obj.update(dt)

        screen.fill([0,0,0])

        for asteroid_obj in asteroids:
            if asteroid_obj.collision_detection(player):
                print("Game over!")
                return
            
            for shot_obj in shots:
                if shot_obj.collision_detection(asteroid_obj):
                    shot_obj.kill()
                    asteroid_obj.split()

            
        

        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        pygame.display.flip()

        dt = asteroids_clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()