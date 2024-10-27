import pygame

class Button:
    def __init__(self, id, image, x, y):
        self.id = id
        self.rect = pygame.Rect(x, y, 72, 72)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (72,72))
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False