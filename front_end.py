import pygame
import input
from player import Player
from sprite import sprites
from button import Button
from Label import Label
from task import Task_list, task
from logic import *
from event import *

modal_needs_drawing = False


class purchase_modal:
    
    def __init__(self, item_id, screen):
        self.id = item_id
        global modal
        modal = pygame.image.load("./assets/cards/payment_modal.png")
        modal = pygame.transform.scale(modal, (800, 600))
        global modal_needs_drawing
        modal_needs_drawing = True
        global purchase_amount 
        purchase_amount = task_list.list[item_id].cost

    def remove_task(self):
        task_list.list.remove(task_list.list[self.id])

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
event_list = Event_panel()

menu_btn = Button(0, "./assets/char/menu_button.png", 480+826, 36)
player_icon = Button(1, "./assets/char/player_icon.png", 480+36, 36)
interact_btn = Button(2, "./assets/char/going_in.png", 480 + 730, 36)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clear_colour = (0,0,0)
running = True
player = Player("./assets/char/player.png", 880, 550, "Toshi")
crdCoords = (36+560,432+276)
crd = Button(0, "./assets/cards/card_credit.png", crdCoords[0], crdCoords[1], 204, 132)
dbt = Button(0, "./assets/cards/card_debit.png", crdCoords[0]+526, crdCoords[1], 204, 132)
#bg map
map = pygame.image.load("./assets/bg/bg_map_moscow.png")
map = pygame.transform.scale(map, (MAIN_PANEL_WIDTH, HEIGHT))

rep = Label(0,f"{player.logic.reputation_status}", 480+36+108, 36, 300, 72, 30)
day = Label(1, str(current_game_day_of_week) , 480 + 72 + 380, 36, 300, 72, 30)

#Mainloop
while running:
    #for events
    calculate_day_of_week()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)
        if menu_btn.is_clicked(event):
            print(True)
        if crd.is_clicked(event):
            if player.logic.purchase(purchase_amount, "credit") == "success":
                print()
                new_modal.remove_task()

            modal_needs_drawing = False
        if dbt.is_clicked(event):
            player.logic.purchase(purchase_amount, "debit")
            if player.logic.purchase(purchase_amount, "credit") == "success":
                new_modal.remove_task()
            modal_needs_drawing = False

        if interact_btn.is_clicked(event):
            hit_building = player.interact()
            building_list = []
            for task in task_list.list:
                building_list.append(task.building)
            if hit_building.number in building_list:
                indx = building_list.index(hit_building.number)
                new_modal = purchase_modal(indx,screen)
                print(indx)

        
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
    event_list.events = player.logic.player_event_list
    event_list.draw(screen)
    
    screen.blit(map, (EVENT_PANEL_WIDTH, 0))
    menu_btn.draw(screen)
    player_icon.draw(screen)
    interact_btn.draw(screen)
    rep.draw(screen, True)
    day.draw(screen, True)
    for s in sprites:
        s.draw(screen)

    if modal_needs_drawing:
        screen.blit(modal, (560, 276))
        crd.draw(screen)
        dbt.draw(screen)
        am = Label(0, f"{purchase_amount}", 650+560, 142+276,200, 36, 30)
        am.draw(screen, False, (255,255,255))
        am = Label(0, f"{player.logic.current_account_balance}", 650+560, 142+276+81,200, 36, 30)
        am.draw(screen, False, (93,89,147))
        am = Label(0, f"{player.logic.card_balance}", 650+560, 142+276+162,200, 36, 30)
        am.draw(screen, False, (93,89,147))
    
    pygame.display.flip()

    pygame.time.delay(10)
pygame.quit()
    
