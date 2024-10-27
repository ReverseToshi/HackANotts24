import pygame
import input
from player import Player
from sprite import sprites
from button import Button
from Label import Label
from task import Task_list, task

#Window dimensions
WIDTH = 1920
HEIGHT = 1080

# Panel dimensions
EVENT_PANEL_WIDTH = 480
INFO_PANEL_WIDTH = 480
MAIN_PANEL_WIDTH = WIDTH - EVENT_PANEL_WIDTH - INFO_PANEL_WIDTH

pygame.init()


#panels
event_panel = pygame.Rect(0, 0, EVENT_PANEL_WIDTH, HEIGHT)
main_panel = pygame.Rect(EVENT_PANEL_WIDTH, 0, MAIN_PANEL_WIDTH, HEIGHT)
task_panel = pygame.Rect(EVENT_PANEL_WIDTH + MAIN_PANEL_WIDTH, 0, INFO_PANEL_WIDTH, HEIGHT)
task_list = Task_list()

menu_btn = Button(0, "./assets/char/menu_button.png", 480+826, 36)
player_icon = Button(1, "./assets/char/player_icon.png", 480+36, 36)
interact_btn = Button(2, "./assets/char/going_in.png", 480 + 730, 36)
rep = Label(0,"Proletarii", 480+36+108, 36, 300, 72, 36)
day = Label(1, "Wednesday", 480 + 36 + 380, 36, 300, 72, 36)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clear_colour = (0,0,0)
running = True
player = Player("./assets/char/player.png", 880, 550)

#bg map
map = pygame.image.load("./assets/bg/bg_map_moscow.png")
map = pygame.transform.scale(map, (MAIN_PANEL_WIDTH, HEIGHT))

#Mainloop
while running:
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
        if interact_btn.is_clicked(event):
            player.interact()
        
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
    pygame.draw.rect(screen, (0, 2, 25), event_panel)  # Event Panel
    pygame.draw.rect(screen, (200,200,200), main_panel)
    pygame.draw.rect(screen, (0, 2, 25), task_panel)   # Info Panel

    task_list.display_task_list(screen)
    
    screen.blit(map, (EVENT_PANEL_WIDTH, 0))
    menu_btn.draw(screen)
    player_icon.draw(screen)
    interact_btn.draw(screen)
    rep.draw(screen, True)
    day.draw(screen, True)
    for s in sprites:
        s.draw(screen)
    
    pygame.display.flip()

    pygame.time.delay(17)
pygame.quit()