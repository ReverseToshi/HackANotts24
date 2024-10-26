import pygame
import input
from player import Player
from sprite import sprites
from map import Map, TileKind


#Window dimensions
WIDTH = 1920
HEIGHT = 1080

# Panel dimensions
EVENT_PANEL_WIDTH = 480
INFO_PANEL_WIDTH = 480
MAIN_PANEL_WIDTH = WIDTH - EVENT_PANEL_WIDTH - INFO_PANEL_WIDTH

pygame.init()

pygame.display.set_caption("HackNotts24")

event_panel = pygame.Rect(0, 0, EVENT_PANEL_WIDTH, HEIGHT)
main_panel = pygame.Rect(EVENT_PANEL_WIDTH, 0, MAIN_PANEL_WIDTH, HEIGHT)
info_panel = pygame.Rect(EVENT_PANEL_WIDTH + MAIN_PANEL_WIDTH, 0, INFO_PANEL_WIDTH, HEIGHT)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clear_colour = (0,0,0)
running = True
player = Player("./assets/char/player.png", 0, 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

    player.update()

    
    screen.fill(clear_colour)
    pygame.draw.rect(screen, (100, 100, 100), event_panel)  # Event Panel
    pygame.draw.rect(screen, (200,200,200), main_panel)
    pygame.draw.rect(screen, (100, 100, 100), info_panel)   # Info Panel
    for s in sprites:
        s.draw(screen)

    pygame.display.flip()

    pygame.time.delay(17)
pygame.quit()