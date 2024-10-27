import pygame
import input
from player import Player
from sprite import sprites
from button import Button

#Window dimensions
WIDTH = 1920
HEIGHT = 1080

# Panel dimensions
EVENT_PANEL_WIDTH = 480
INFO_PANEL_WIDTH = 480
MAIN_PANEL_WIDTH = WIDTH - EVENT_PANEL_WIDTH - INFO_PANEL_WIDTH

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("HackNotts24")

#panels
event_panel = pygame.Rect(0, 0, EVENT_PANEL_WIDTH, HEIGHT)
main_panel = pygame.Rect(EVENT_PANEL_WIDTH, 0, MAIN_PANEL_WIDTH, HEIGHT)
info_panel = pygame.Rect(EVENT_PANEL_WIDTH + MAIN_PANEL_WIDTH, 0, INFO_PANEL_WIDTH, HEIGHT)
menu_btn = Button(0, "./assets/char/menu_button.png", 480+816, 36)
player_icon = Button(1, "./assets/char/player_icon.png", 480+36, 36)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clear_colour = (0,0,0)
running = True
player = Player("./assets/char/player.png", 880, 550)

#bg map
map = pygame.image.load("./assets/bg/bg_map_moscow.png")
map = pygame.transform.scale(map, (MAIN_PANEL_WIDTH, HEIGHT))



#Mainloop
while running:
    old_pos = (player.x, player.y)
    delta_time = clock.tick(30) / 1000
    
    #for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)
        if menu_btn.is_clicked(event):
            print(True)
        
    #for player movements
    if player.x > EVENT_PANEL_WIDTH + MAIN_PANEL_WIDTH - 50:
        player.x -= player.movement_speed
    if player.x < EVENT_PANEL_WIDTH:
        player.x += player.movement_speed
    if player.y < 0:
        print(player.y)
        player.y += player.movement_speed
    if player.y > HEIGHT - 80:
        print(player.y)
        player.y -= player.movement_speed

    player.update()

    #drawing screen
    screen.fill(clear_colour)
    pygame.draw.rect(screen, (100, 100, 100), event_panel)  # Event Panel
    pygame.draw.rect(screen, (200,200,200), main_panel)
    pygame.draw.rect(screen, (100, 100, 100), info_panel)   # Info Panel

    
    screen.blit(map, (EVENT_PANEL_WIDTH, 0))
    menu_btn.draw(screen)
    player_icon.draw(screen)
    for s in sprites:
        s.draw(screen)
    
    pygame.display.flip()

    pygame.time.delay(17)
pygame.quit()