import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
##########################################################################
pygame.init()
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
refresh = True

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroidfield = AsteroidField()
##########################################################################
while refresh:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            refresh = False
    
    screen.fill(000000)

    updatable.update(dt)
    for thing in asteroids:
        if thing.check_for_collisions(player) == True:
            log_event("player_hit")
            print("Game over!")
            sys.exit()
        for shot in shots:
            if thing.check_for_collisions(shot) == True:
                log_event("asteroid_shot")
                thing.split()
                shot.kill()

    for thing in drawable:
        thing.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
