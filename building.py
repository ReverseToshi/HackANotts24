import pygame

class building:
    def __init__(self, id, x, y, w, h, friendly_name):
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.friendly_name = friendly_name