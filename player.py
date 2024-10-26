import pygame
from sprite import Sprite
from input import is_key_pressed

class Player(Sprite):
    size = 20
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.movement_speed = 2
    
    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= self.movement_speed
        if is_key_pressed(pygame.K_s):
            self.y += self.movement_speed
        if is_key_pressed(pygame.K_a):
            self.x -= self.movement_speed
        if is_key_pressed(pygame.K_d):
            self.x += self.movement_speed
        
        