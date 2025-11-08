import pygame
import circleshape
import random
from logger import log_event
from constants import *

class Asteroid(circleshape.CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_angle00 = self.velocity.rotate(random_angle)
        new_angle01 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid00 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid01 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid00.velocity = new_angle00 * 1.2
        new_asteroid01.velocity = new_angle01 * 1.2