import pygame
from circleShape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        current_position = self.position
        base_velocity = self.velocity
        old_radius = self.radius
        
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        new_angle = random.uniform(20,50)
        vector1 = base_velocity.rotate(new_angle)
        vector2 = base_velocity.rotate(-new_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(current_position.x, current_position.y, new_radius)
        new_asteroid1.velocity = vector1 * 1.2 

        new_asteroid2 = Asteroid(current_position.x, current_position.y, new_radius)
        new_asteroid2.velocity = vector2 * 1.2



        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt