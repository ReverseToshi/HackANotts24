import pygame
from Label import Label

class Event:
    def __init__(self, day_of_week, score_change, description):
        self.day = day_of_week
        self.change = score_change
        self.description = description
    
    def publish_event():
        # code to publish this event so that it reaches the frontend code
        pass

class Event_panel:
    def __init__(self):
        self.events = [Event("Monday", "+20", "Got interest")]
        self.header = Label(5, "Transactions", 36, 36, 100, 72, 30)
        self.x = 36
    
    def add_events(self, Event):
        self.events.append(Event)
        if len(self.events) > 8:
            self.events.remove(self.events[0])

    def draw(self, screen):
        self.header.draw(screen, False, (255,255,255))
        for event in self.events:
            i = self.events.index(event)
            y = 1000-i*72
            Label(6, event.day, self.x, y, 100, 5, 10).draw(screen, False, (66,71,131))
            Label(6, event.description, self.x, y+5, 100, 30, 20).draw(screen, False, (255,255,255))
    