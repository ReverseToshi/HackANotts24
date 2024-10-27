import pygame

class Label:
    def __init__(self, id, text, x, y, w, h, font_size):
        self.id = id
        self.text = text
        self.x = x
        self.y = y
        self.h = h
        self.w= w
        self.font = pygame.font.Font("./assets/type/Pixeled.ttf", font_size)


    def draw(self, screen, bg=False, fg = (0, 0, 0)):
        if bg:
            bgr = (255,255,255)
        else:
            bgr = None
        text_surface = self.font.render(self.text, True, fg, bgr)
        text_x = self.x
        text_y = self.y
        screen.blit(text_surface,(text_x, text_y))
