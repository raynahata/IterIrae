#useful imports:
import pygame
import os
import sys
from Sprites import *
from base import BaseState

class LevelTwo(BaseState):

    kitchen_platforms = pygame.sprite.Group()
    knives = pygame.sprite.Group()
    jemsList = pygame.sprite.Group()
    feet = pygame.sprite.Group()
    cheeses = pygame.sprite.Group()
    feet_other = pygame.sprite.Group()

    
    def __init__(self):
        super(LevelTwo, self).__init__()
        
        self.screenHeight = self.screen_rect.height
        self.screenWidth = self.screen_rect.width

        
        self.background = pygame.image.load("background_kitchen.png")
        self.background = pygame.transform.scale(self.background,(self.screenWidth,self.screenHeight))
        
        kitchen1 = Platform(0,(self.screenHeight*0.86), "platforms/kitchen1.png")
        kitchen1.image = pygame.transform.scale(kitchen1.image, (kitchen1.image.get_width()*1.4, kitchen1.image.get_height()*1.4))
        kitchen1.rect = kitchen1.image.get_rect(topleft = (0,self.screenHeight*0.86))
        
        kitchen2 = Platform(self.screenWidth*0.61, self.screenHeight*0.86, "platforms/kitchen1.png")
        kitchen2.image = pygame.transform.scale(kitchen2.image, (kitchen2.image.get_width()*1.4, kitchen2.image.get_height()*1.4))
        kitchen2.rect = kitchen2.image.get_rect(topleft = (self.screenWidth*0.61, self.screenHeight*0.86))
        
        kitchen3 = Platform(self.screenWidth*0.43, self.screenHeight*0.75, "platforms/kitchen2.png")
        
        kitchen4 = Platform(0, self.screenHeight*0.45, "platforms/kitchen3.png")
        kitchen4.image = pygame.transform.scale(kitchen4.image, (kitchen4.image.get_width()*1.5, kitchen4.image.get_height()*1.2))
        kitchen4.rect = kitchen4.image.get_rect(topleft = (0, self.screenHeight*0.45))
        
        kitchen5 = Platform(self.screenWidth*0.75, self.screenHeight*0.55, "platforms/kitchen4.png")
        
        kitchen6 = Platform(self.screenWidth*0.4, self.screenHeight*0.25, "platforms/kitchen4.png")
        
        kitchen7 = Platform(self.screenWidth*0.65, self.screenHeight*0.15, "platforms/kitchen3.png")
        kitchen7.image = pygame.transform.scale(kitchen7.image, (kitchen7.image.get_width()*1.5, kitchen7.image.get_height()*1.2))
        kitchen7.rect = kitchen7.image.get_rect(topleft = (self.screenWidth*0.65, self.screenHeight*0.15))
        
        kitchen8 = Platform(0, self.screenHeight*0.1, "platforms/kitchen2.png")
        kitchen8.image = pygame.transform.scale(kitchen8.image, (kitchen8.image.get_width()*1.6, kitchen8.image.get_height()))
        kitchen8.rect = kitchen8.image.get_rect(topleft = (0, self.screenHeight*0.1))
        
        kitchen9 = Platform(self.screenWidth*0.58, self.screenHeight*0.65, "platforms/kitchen2.png")
        
        kitchen10 = Platform(self.screenWidth*0.38, self.screenHeight*0.55, "platforms/kitchen2.png")
        
        kitchen11 = Platform(self.screenWidth*0.2, self.screenHeight*0.33, "platforms/kitchen2.png")
        
        kitchen12 = Platform(self.screenWidth*0.27, self.screenHeight*0.17, "platforms/kitchen2.png")
        kitchen12.image = pygame.transform.scale(kitchen12.image, (kitchen12.image.get_width()*0.5, kitchen12.image.get_height()))
        kitchen12.rect = kitchen12.image.get_rect(topleft = (self.screenWidth*0.27, self.screenHeight*0.17))


        self.kitchen_platforms.add(kitchen1)
        self.kitchen_platforms.add(kitchen2)
        self.kitchen_platforms.add(kitchen3)
        self.kitchen_platforms.add(kitchen4)
        self.kitchen_platforms.add(kitchen5)
        self.kitchen_platforms.add(kitchen6)
        self.kitchen_platforms.add(kitchen7)
        self.kitchen_platforms.add(kitchen8)
        self.kitchen_platforms.add(kitchen9)
        self.kitchen_platforms.add(kitchen10)
        self.kitchen_platforms.add(kitchen11)
        self.kitchen_platforms.add(kitchen12)
        
        
        jem1 = Jems(0, self.screenHeight*0.78)
        jem2 = Jems(0, self.screenHeight*0.38)
        jem3 = Jems(self.screenWidth*0.9, self.screenHeight*0.08)
        
        self.jemsList.add(jem1)
        self.jemsList.add(jem2)
        self.jemsList.add(jem3)
        
        knife1 = Knife(self.screenWidth*0.1, self.screenHeight*0.83)
        knife2 = Knife(self.screenWidth*0.11, self.screenHeight*0.83)
        knife3 = Knife(self.screenWidth*0.12, self.screenHeight*0.83)
        knife4 = Knife(self.screenWidth*0.1, self.screenHeight*0.42)
        knife5 = Knife(self.screenWidth*0.11, self.screenHeight*0.42)
        knife6 = Knife(self.screenWidth*0.12, self.screenHeight*0.42)
        knife7 = Knife(self.screenWidth*0.85, self.screenHeight*0.12)
        knife8 = Knife(self.screenWidth*0.86, self.screenHeight*0.12)
        knife9 = Knife(self.screenWidth*0.87, self.screenHeight*0.12)
        
        self.knives.add(knife1)
        self.knives.add(knife2)
        self.knives.add(knife3)
        self.knives.add(knife4)
        self.knives.add(knife5)
        self.knives.add(knife6)
        self.knives.add(knife7)
        self.knives.add(knife8)
        self.knives.add(knife9)

       

        foot = Foot(self.screenWidth*0.3, self.screenHeight*0.68)
        self.feet.add(foot)
        
        other_foot = Foot(self.screenWidth*0.17,0)
        self.feet_other.add(other_foot)
        
        cheese = Cheese(0, self.screenHeight*0.03)
        self.cheeses.add(cheese)
        

        self.player.rect.x= self.screenWidth*0.8
        self.player.rect.y= self.screenHeight*0.8
        
        self.refresh = []

        self.previousKey= ' '
        
        
        if(self.player.speed == 1):
            self.playerStepLength=self.screenWidth/30#player step distance
        if(self.player.speed == 2):
            self.playerStepLength=self.screenWidth/20#player step distance
        
        if(self.player.highjump == 1):
            self.playerJumpLength=self.screenHeight/20
        if(self.player.highjump == 2):
            self.playerJumpLength = self.screenHeight/10
            
        self.clock = pygame.time.Clock()
        
       
        
    def draw(self, screen):
        
        self.get_conditionals()
        
        self.player.update()
        self.refresh.append(self.player.rect)
        
        screen.blit(self.background,(0,0))
        screen.blit(self.player.image, self.player.rect)
        self.kitchen_platforms.draw(screen)
        self.jemsList.draw(screen)
        self.knives.draw(screen)
        self.feet.draw(screen)
        self.feet_other.draw(screen)
        self.cheeses.draw(screen)

        
    def get_conditionals(self):
        
        #testing to see if player hit bottom of screen
        if(self.player.rect.y == self.screenHeight-61):
            print("The player has fallen down")
            
            self.done=True
            self.next_state="MainPage"
            pygame.mixer.pause()
            mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
            pygame.mixer.Sound.play(mainPageSound,-1) 
            self.player.rect.x= self.screenWidth*0.8
            self.player.rect.y= self.screenHeight*0.8
    
        #platform collision
        collisionPlatform = pygame.sprite.spritecollideany(self.player,self.kitchen_platforms)
        if(collisionPlatform != None):
            if(self.player.rect.bottom >= collisionPlatform.rect.top and self.player.rect.bottom <= collisionPlatform.rect.bottom):
                self.player.inAir=False
            if(self.player.rect.top <= collisionPlatform.rect.bottom and self.player.rect.bottom >= collisionPlatform.rect.bottom):
                self.player.inAir=True
        else:
            self.player.inAir = True
    
        #foot dropping
        for i in self.feet:
            if i.rect.y >= self.screenHeight*0.8:
                i.rect.y = self.screenHeight*(0.68)
                self.refresh.append(i.rect)
            i.moveDown(1)
            i.update()
            self.refresh.append(i.rect)
            
        #other foot dropping
        for i in self.feet_other:
            if i.rect.y >= self.screenHeight*0.38:
                i.rect.y = 0
                self.refresh.append(i.rect)
            i.moveDown(1)
            i.update()
            self.refresh.append(i.rect)
        
        if(self.player.inAir==True):
            if(self.player.rect.y<self.screenHeight)-10:
                self.player.gravity()
            self.refresh.append(self.player.rect)

        if(self.player.rect.y>self.screenHeight-10):
            self.player.inAir=False
            self.player.rect.clamp_ip(self.screen_rect)
            self.refresh.append(self.player.rect)
        
    def get_event(self, event):
        
        keys = pygame.key.get_pressed()
                
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
            
        #checking for jem collision
        collisionJemItem=pygame.sprite.spritecollideany(self.player, self.jemsList)
        if(collisionJemItem!=None):
            gemCollection = pygame.mixer.Sound("Sounds/reward.wav") # defines the sound
            pygame.mixer.Sound.play(gemCollection) 
            collisionJemItem.kill()
            self.player.increaseJem(1)
            print(self.player.jems)
        else:
            for i in self.jemsList:
                self.refresh.append(i.rect)
                
        #cheese collision
        collisioncheese = pygame.sprite.spritecollideany(self.player, self.cheeses)
        if(collisioncheese != None):
            print("went to finish page")
            self.done=True
            self.clock.tick()
            self.player.time=self.clock.get_time()/1000
            self.next_state="FinishPage"
            pygame.mixer.pause()
            finalCheese = pygame.mixer.Sound("Sounds/finalCheese.wav") # defines the sound
            pygame.mixer.Sound.play(finalCheese) 
            self.player.rect.x= self.screenWidth*0.8
            self.player.rect.y= self.screenHeight*0.8
            
        else:
            for i in self.cheeses:
                self.refresh.append(i.rect)
                
        #knife collision
        collisionKnifeItem = pygame.sprite.spritecollideany(self.player,self.knives)
        if(collisionKnifeItem != None):
            print("player has been killed")
            pygame.mixer.pause()

            knifeSound = pygame.mixer.Sound("Sounds/knife.wav") # defines the sound
            pygame.mixer.Sound.play(knifeSound)
            self.done=True
            self.next_state="MainPage"
            mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
            pygame.mixer.Sound.play(mainPageSound,-1)
            self.player.rect.x= self.screenWidth*0.8
            self.player.rect.y= self.screenHeight*0.8
            
        else:
            for i in self.knives:
                self.refresh.append(i.rect)




            
        #foot collision
        collisionfoot_otherItem = pygame.sprite.spritecollideany(self.player,self.feet_other)
        if(collisionfoot_otherItem != None):
            print("player has been killed")
            self.done=True
            self.next_state="MainPage"
            self.player.rect.x= self.screenWidth*0.8
            self.player.rect.y= self.screenHeight*0.8
        else:
            for i in self.feet_other:
                self.refresh.append(i.rect)
        collisionfootItem = pygame.sprite.spritecollideany(self.player,self.feet)
        if(collisionfootItem != None):
            print("player has been killed")
            self.done=True
            self.next_state="MainPage"
            pygame.mixer.pause()
            footSound = pygame.mixer.Sound("Sounds/chefFeet.wav") # defines the sound
            pygame.mixer.Sound.play(footSound)

            mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
            pygame.mixer.Sound.play(mainPageSound,-1) 
            self.player.rect.x= self.screenWidth*0.8
            self.player.rect.y= self.screenHeight*0.8
            
        else:
            for i in self.feet:
                self.refresh.append(i.rect)
                
        #key inputs
        if keys[pygame.K_a]:
            print('left')
           
            if(self.player.rect.x>=0 and self.player.rect.x<self.screenWidth):
                self.player.move_left(self.playerStepLength)
              
            else:
                self.player.rect.clamp_ip(self.screen_rect)
            
            self.refresh.append(self.player.rect)

        if keys[pygame.K_d]:
            print('right')
           
            if(self.player.rect.x>=0 and self.player.rect.x<(self.screenWidth-self.player.rect.width)):
                self.player.move_right(self.playerStepLength)
                
            else:
                self.player.rect.clamp_ip(self.screen_rect)
                    
            self.refresh.append(self.player.rect)
             

        if keys[pygame.K_w]:
            print('jump')

            if(self.player.rect.y>=0 and self.player.rect.y<self.screenHeight and self.player.inAir == False):
                self.player.move_up(self.playerJumpLength)
                
            else:
                self.player.rect.clamp_ip(self.screen_rect) #keeping the rat within the border of the screen rect 
           
            self.refresh.append(self.player.rect)
            

         #game ending condition 
        if keys[pygame.K_q]:
            print("Game has been quit. Thanks for playing!")
            print(self.player.jems)
            self.done=True
            self.next_state="MainPage"
         
            #pygame.quit()
            #sys.exit()
            #main = False
    
        
    
        
        
        
        
    
