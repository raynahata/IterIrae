#Rayna Hata 
#IterIrae Play game page 

from MainPage import *
from InfoPage import *
from upgrades import * 
from Sprites import *
from game import *
from level_one import *
from level_two import * 
from FinishPage import *

import pygame as pg
import sys 



pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 60)

screen = pygame.display.set_mode((1440,750))
states = {
    "MainPage": MainPage(),
    "InfoPage": InfoPage(),
    "Upgrades": Store(),
    "LevelOne": LevelOne(),
    "LevelTwo": LevelTwo(),
    "FinishPage": FinishPage()
  
}

game = Game(screen, states, "MainPage")
game.run()

pygame.quit()
sys.exit()