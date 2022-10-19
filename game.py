#imported from https://github.com/ianrufus/youtube/blob/main/pygame-state/game.py
#modifed by Rayna Hata 


import pygame
import sys
from Sprites import *




class Game(object):
    pygame.mixer.init()
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]
        self.reset=True

        
    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self):
        print(self.state.player.jems)
        newJems=self.state.player.jems 
        newHearts=self.state.player.Hearts
        newSpeed=self.state.player.speed
        newJump=self.state.player.highjump 
        newTime=self.state.player.time
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)
        self.reset=True 
        self.state.player.jems=newJems
        self.state.player.Hearts=newHearts
        self.state.player.speed=newSpeed
        self.state.player.highjump=newJump
        self.state.player.time=newTime

        
            

        
        print(self.state.player.jems)


    def update(self, dt):
        if self.state.quit:
            self.done = True

        elif self.state.done:
            self.flip_state()
            self.reset=True

        self.state.update(dt)


    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()

    
