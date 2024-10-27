import pygame
from sprite import Sprite
from input import is_key_pressed
from building import building
from logic import logic

# buildings
buildings = [building("Apartment", 480+108, 192, 132, 288, "Apartment", 0),
             building("Grocery", 480+48, 528, 144, 144, "Grocerov", 1),
             building("Bakery", 480+48, 720, 144, 96, "Breadnik", 2),
             building("Bank", 480+48, 864, 396, 168, "Gosbank", 3),
             building("Autoshop", 480+492, 864, 216, 168, "Lada DeaLership", 4),
             building("Bunker", 480+792, 924, 120, 108, "Nina's Bunker", 5),
             building("Technology", 480+804, 648, 108, 168, "Techno Store", 6),
             building("University", 480+756, 288, 156, 312, "University", 7),
             building("Party HQ", 480+600, 96, 108, 288, "Stary Senat", 8),
             building("Gulag", 480+288, 192, 264, 192, "GuLag", 9)]

class Player(Sprite):

    size = 20
    def __init__(self, image, x, y, name):
        super().__init__(image, x, y)
        self.movement_speed = 4
        self.logic = logic(name)
    
    def update(self):
        self.old_pos=(self.x, self.y)
        if is_key_pressed(pygame.K_w):
            self.y -= self.movement_speed
        if is_key_pressed(pygame.K_s):
            self.y += self.movement_speed
        if is_key_pressed(pygame.K_a):
            self.x -= self.movement_speed
        if is_key_pressed(pygame.K_d):
            self.x += self.movement_speed
        self.if_collision()

        # backend update stuff
        self.logic.calculate_cur()
        self.logic.check_status()
    
    def if_collision(self):
        for blding in buildings:
            if self.x in range(blding.x-20, blding.x+blding.w) and self.y in range(blding.y -60, blding.y+blding.h):
                self.x = self.old_pos[0]
                self.y = self.old_pos[1]
        else:
            return None
    
    def interact(self):
        for blding in buildings:
            if self.x in range(blding.x-22, blding.x+blding.w +22) and self.y in range(blding.y -60 -22, blding.y+blding.h+22):
                # print(blding.friendly_name)
                return blding
        else:
            return None
                    
