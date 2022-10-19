# Daniel Tarkoff
# IterIrae 
# Finish Page 


import sys
import pygame
from base import BaseState
from Sprites import *
from pygame import mixer



class FinishPage(BaseState):
    buttons=pygame.sprite.Group()
    
    pygame.init()
    pygame.font.init()
   


    def __init__(self):
        super(FinishPage, self).__init__()
        self.active_index = 0
        self.options = ["ReturnHome"]
        self.next_state = "MainPage"

        self.screenHeight=self.screen_rect.height
        self.screenWidth=self.screen_rect.width



        self.background=pygame.image.load('Finish/finish.png')
        self.background= pygame.transform.scale(self.background,(self.screenWidth,self.screenHeight)) 

        #creating the buttons 
        self.ratImage = FinishPageSprites('ratImage', self.screenWidth * 0.44, self.screenHeight * 0.5605, 2, 'Finish/rat1.png')
        self.buttons.add(self.ratImage)

        # drawing the score-board box
        self.scoreBox = FinishPageSprites('scoreBox', self.screenWidth*0.25, self.screenHeight*0.2, 0.7, 'Finish/ScoreBox.png')
        self.buttons.add(self.scoreBox)
        

        
        self.returnToMain = FinishPageSprites('returnToMain', self.screenWidth*0.08, self.screenHeight*0.751, 0.8, 'Finish/tower return button.png')
        self.buttons.add(self.returnToMain)

        self.nextLevel = FinishPageSprites('nextLevel', self.screenWidth*0.9, self.screenHeight*0.751, 0.8, 'Finish/tower return button.png')
        self.buttons.add(self.nextLevel)

    
    def draw(self,screen):
        screen.blit(self.background,(0,0))
        self.buttons.draw(screen)

        # writing the score:
        black = (0, 0, 0)
        font = pygame.font.SysFont(None, 80)
        img = font.render(format(self.player.time), True, black) # changing "hello" into whatever the global variable for the score is
        screen.blit(img, (625, 300))
     

    def get_event(self,event):
    
        event.type==pygame.mouse.set_visible(True)
    
        keys = pygame.key.get_pressed()
        tpos = pygame.mouse.get_pos()

            
           
        if(event.type==pygame.MOUSEBUTTONDOWN):
             for box in self.buttons:      
                if box.rect.collidepoint(tpos): 
                    if(box.name== "returnToMain"):
                        print("you clicked return") 
                        self.next_state="MainPage" 
                        self.done=True
                        
                        pygame.mixer.pause() # stops all sounds  
                        mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
                        pygame.mixer.Sound.play(mainPageSound,-1)
                    elif(box.name== "nextLevel"):
                        print("you clicked next level") 

                        self.next_state="LevelTwo" # CHANGE: to level 2 name
                        self.done=True
                        
                        pygame.mixer.pause() # stops all sounds  
                        KitchenSound = pygame.mixer.Sound("Sounds/kitchenSoundTrack.wav") # defines the sound
                        pygame.mixer.Sound.play(KitchenSound,-1)    
                    
        
        if keys[pygame.K_q]:
            print("Game has been quit. Thanks for playing!")
            self.done=True
            self.next_state="MainPage"
            pygame.mixer.pause()
            mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
            pygame.mixer.Sound.play(mainPageSound,-1) 
            #pygame.mixer.Sound.stop(self.sewerSound)
            #pygame.mixer.Sound.play(self.mainPageSound)

        


   















 


               

    
        
