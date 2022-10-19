#Rayna Hata 
#IterIrae 
#Main Page 


import sys
import pygame
from base import BaseState
from Sprites import *



class MainPage(BaseState):
    buttons=pygame.sprite.Group()
    pygame.mixer.init()
    pygame.mixer.pause() # stops all sounds  
    mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
    pygame.mixer.Sound.play(mainPageSound,-1)

    def __init__(self):
        super(MainPage, self).__init__()
        # self.player=Player(0,0)
        self.active_index = 0
        self.options = ["LevelOne", "Upgrades", "InfoPage", ]
        self.next_state = "LevelOne"

        self.screenHeight=self.screen_rect.height
        self.screenWidth=self.screen_rect.width
        



        self.background=pygame.image.load('MainPage/MainPage.png')
        self.background= pygame.transform.scale(self.background,(self.screenWidth,self.screenHeight)) 

        #creating the buttons 
        self.sewer=MainPageSprites('sew',self.screenWidth*0.65,self.screenHeight*0.62,0.65,'MainPage/sewer.png')
        self.armory=MainPageSprites('armory',self.screenWidth*0.65,self.screenHeight*0.48,0.65,'MainPage/armory.png')
        self.kitchen=MainPageSprites('kitchen',self.screenWidth*0.65,self.screenHeight*0.32,0.65,'MainPage/kitchen.png')
        self.upgrade=MainPageSprites('upgrade',self.screenWidth*0.83,self.screenHeight*0.05,0.5,'MainPage/upgrades.png')
        self.instr=MainPageSprites('instr',self.screenWidth*0.02,self.screenHeight*0.9,0.4,'MainPage/instructions.png')

        self.buttons.add(self.sewer)
        self.buttons.add(self.armory)
        self.buttons.add(self.kitchen)
        self.buttons.add(self.upgrade)
        self.buttons.add(self.instr)
        
        
        #pygame.mixer.Sound.play(self.mainPageSound)
           
    
    def draw(self,screen):
        #pygame.mixer.Sound.stop(self.sewerSound)
        screen.blit(self.background,(0,0))
        self.buttons.draw(screen)
     

    def get_event(self,event):
        
        #pygame.mixer.music.play()
        event.type==pygame.mouse.set_visible(True)
    
        keys = pygame.key.get_pressed()
        tpos = pygame.mouse.get_pos()
           
           
        if(event.type==pygame.MOUSEBUTTONDOWN):
             for box in self.buttons:      
                if box.rect.collidepoint(tpos): 
                    if(box.name=='upgrade'):
                        print("you clicked upgrades") 
                        
                        self.next_state="Upgrades" 
                        self.done=True
                        pygame.mixer.pause()
                        mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
                        pygame.mixer.Sound.play(mainPageSound,-1) 
                    if(box.name=='instr'):
                        print("you clicked info") 
            
                        self.next_state="InfoPage" 
                        self.done=True
                        pygame.mixer.pause()
                        mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
                        pygame.mixer.Sound.play(mainPageSound,-1) 
                    if(box.name=='sew'):
                        print("you clicked sewer") 
            
                        self.next_state="LevelOne" 
                        self.done=True
                        #self.mainPageSound.stop()
                        pygame.mixer.pause() # stops all sounds  
                        levelOneSound = pygame.mixer.Sound("Sounds/sewerSoundtrack.wav") # defines the sound
                        pygame.mixer.Sound.play(levelOneSound,-1) 


        if keys[pygame.K_q]:
            self.quit=True
            pygame.quit()
            sys.exit()                 
        
        
   


        


   















 


               

    
        
