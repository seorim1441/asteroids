# This allows us to use code from the open-source
# pygame library throughout this file
import pygame
from constants import *
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
refresh = True

while refresh:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            refresh = False
    screen.fill(000000)
    pygame.display.flip()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
