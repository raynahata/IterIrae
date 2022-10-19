#imported from https://github.com/ianrufus/youtube/blob/main/pygame-state/states/base.py
import pygame
from Sprites import * 


class BaseState(object):
    
    def __init__(self):
        
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(None, 24)
        self.player=Player(0,0)
        self.JumpHeight=self.player.highjump
        self.speed=self.player.speed
        self.jems=self.player.jems
        self.time=0

        
        
        
        
   
    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass

    def updatePlayerStats(self):
        pass

