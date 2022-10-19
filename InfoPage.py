#Rayna Hata 
#IterIrae 
#Info Page 

#Rayna Hata 
#IterIrae 
#Main Page 


import sys
import pygame
from base import BaseState
from game import *

from Sprites import *


#pygame.init()

class InfoPage(BaseState):
    buttons=pygame.sprite.Group()
    def __init__(self):
        super(InfoPage, self).__init__()
        self.active_index = 0
        self.options = ["Return"]
        self.next_state = "MainPage"
        
        #screenSize=pygame.display.Info() 

        self.screenHeight=self.screen_rect.height
        self.screenWidth=self.screen_rect.width
     

        self.background=pygame.image.load('Info/Info.png')
        self.background= pygame.transform.scale(self.background,(self.screenWidth,self.screenHeight)) 

        #creating the buttons 
        self.backButton=InfoPageSprites('back',self.screenWidth*0.2,self.screenHeight*0.8,0.8,'Info/backButton.png')
        

        self.buttons.add(self.backButton)

    def draw(self,screen):
    
        screen.blit(self.background,(0,0))
        self.buttons.draw(screen)



    def get_event(self,event):
        
        
        pygame.mouse.set_visible(True)
       
        keys = pygame.key.get_pressed()
        tpos = pygame.mouse.get_pos()
        
        if(event.type==pygame.MOUSEBUTTONDOWN):
            for box in self.buttons:
                
                if box.rect.collidepoint(tpos): 
                    if(box.name=='back'):
                        self.next_state="MainPage" 
                        self.done=True
                        print("you are returning to the main screen")

                    
                    
        

        elif event.type == pygame.KEYUP:

            if event.key==keys[pygame.K_q]:
                print("Game has been quit. Thanks for playing!")
                self.quit=True



        


   















 


               

    
        
