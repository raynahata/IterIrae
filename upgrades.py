#Rayna Hata 
#IterIrae 
#Upgrades Page 


import sys
import pygame
from base import BaseState
from game import *

from Sprites import *


#pygame.init()


class Store(BaseState):
    buttons=pygame.sprite.Group()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 60)


    def __init__(self):
        super(Store, self).__init__()
        self.active_index = 0
        self.options = ["Return"]
        self.next_state = "MainPage"
    
        self.screenHeight=self.screen_rect.height
        self.screenWidth=self.screen_rect.width

       


        self.background=pygame.image.load('Store/background.png')
        self.background= pygame.transform.scale(self.background,(self.screenWidth,self.screenHeight)) 

        #creating the buttons 
        self.back=UpgradesPageSprites('back',self.screenWidth*0.1,self.screenHeight*0.8,0.8,'Store/backButton.png')
        self.speed=UpgradesPageSprites('speed',self.screenWidth*0.2,self.screenHeight*0.07,0.8,'Store/speedBoost.png')
        self.jump=UpgradesPageSprites('jump',self.screenWidth*0.43,self.screenHeight*0.09,0.8,'Store/highJump.png')
        self.life=UpgradesPageSprites('life',self.screenWidth*0.7,self.screenHeight*0.1,0.8,'Store/extraLife.png')
        self.jem=UpgradesPageSprites('jem',self.screenWidth*0.3,self.screenHeight*0.5,1,'jems.png')

        self.buttons.add(self.back)
        self.buttons.add(self.life)
        self.buttons.add(self.jump)
        self.buttons.add(self.speed)
        self.buttons.add(self.jem)
        
    def draw(self,screen):
        screen.blit(self.background,(0,0))
       
        self.buttons.draw(screen)
        text_render = self.render_text()
        screen.blit(text_render,(self.screenWidth*0.27,self.screenHeight*0.5))
   

    def render_text(self):
        color = pygame.Color("black")
        numJems=self.player.jems
        return self.myfont.render(format(numJems), True, color)

    
    
    def get_event(self,event):
       

       
        pygame.mouse.set_visible(True)
        # get the mouse position and put the broom so it is centered on the
        # mouse location
       
        
           
        keys = pygame.key.get_pressed()
        tpos = pygame.mouse.get_pos()
            # handle events and erase things
        if(event.type==pygame.MOUSEBUTTONDOWN):
            for box in self.buttons:
                
                if box.rect.collidepoint(tpos): 
                    if(box.name=='speed'):
                        print("you clicked speed")
                        if(self.player.jems>=1):
                            self.player.increaseSpeed()
                            self.player.decreaseJem(1)
                        else:
                            print("you do not heve enough gems")



                    elif(box.name=='back'):
                        print("You are returning to the main page")
                        self.next_state="MainPage" 
                        self.done=True
                        pygame.mixer.pause() # stops all sounds  
                        mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
                        pygame.mixer.Sound.play(mainPageSound,-1)
                    elif(box.name=='jump'):
                        print("you clicked jump")
                        if(self.player.jems>=2):
                            self.player.increaseJump()
                            print(self.player.highjump)
                            self.player.decreaseJem(2)
                        else:
                            print("you do not heve enough gems")
                            

                    elif(box.name=='life'):
                        print("you clicked life")
                        if(self.player.jems>=3):
                            self.player.increaseHeart()
                            self.player.decreaseJem(3)
                        else:
                            print("you do not heve enough gems")
                            

        if event.type == pygame.KEYUP:

            if event.key==keys[pygame.K_q]:
                print("Game has been quit. Thanks for playing!")
                self.quit=True
                pygame.mixer.pause() # stops all sounds  
                mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
                pygame.mixer.Sound.play(mainPageSound,-1)




        


   















 


               

    
        
