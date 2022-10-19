#useful imports
import pygame
import os
import sys
from base import BaseState
from Sprites import *


class LevelOne(BaseState):
    pygame.mixer.init()
    platforms = pygame.sprite.Group()
    AcidDrips = pygame.sprite.Group()
    JemsList = pygame.sprite.Group()
    LeverList = pygame.sprite.Group()
    Doors = pygame.sprite.Group()
    
    
    
    def __init__(self):
        super(LevelOne, self).__init__()
        self.screenHeight=self.screen_rect.height
        self.screenWidth=self.screen_rect.width
        
        
        
        self.background = pygame.image.load("background_sewer.png")
        self.background = pygame.transform.scale(self.background,(self.screenWidth,self.screenHeight))
        
        platform1 = Platform(0,(self.screenHeight*(0.8)),"platforms/Untitled__12.png")
        platform2 = Platform(self.screenWidth*(0.35),self.screenHeight*(0.8),"platforms/Untitled__13.png")
        platform3 = Platform(self.screenWidth*(0.7),self.screenHeight*(0.7),"platforms/Untitled__14.png")
        platform4 = Platform(0,self.screenHeight*(0.6),"platforms/Untitled__10.png")
        platform5 = Platform(0,self.screenHeight*(0.09),"platforms/Untitled__5.png")
        platform6 = Platform(self.screenWidth*(0.38),self.screenHeight*(0.35), "platforms/Untitled__11.png")
        platform6.image = pygame.transform.flip(platform6.image,True,False)
        platform7 = Platform(self.screenWidth*(0.85), self.screenHeight*(0.35),"platforms/Untitled__8.png")
        platform8 = Platform(self.screenWidth*(0.5),self.screenHeight*(0.27),"platforms/Untitled__3.png")
        platform9 = Platform(self.screenWidth*(0.62),self.screenHeight*(0.2),"platforms/Untitled__9.png")
        platform10 = Platform(self.screenWidth*(0.8),self.screenHeight*(0.1),"platforms/Untitled__4.png")
        platform11 = Platform(self.screenWidth*(0.8),self.screenHeight*(0.1),"platforms/Untitled__7.png")
        platform12 = Platform(self.screenWidth*(0.9),self.screenHeight*(0.1),"platforms/Untitled__2.png")
        platform13 = Platform(self.screenWidth*(0.9),self.screenHeight*(0.17),"platforms/Untitled__6.png")
        platform14 = Platform(self.screenWidth*(0.95),self.screenHeight*(0.25),"platforms/Untitled_.png")
        platform15 = Platform(self.screenWidth*(0.55), self.screenHeight*(0.75), "platforms/Untitled__6.png")
        platform15.image = pygame.transform.scale(platform15.image,(platform15.image.get_width()*(1.3), platform15.image.get_height()*(1.3)))
        platform15.rect = platform15.image.get_rect(topleft = (self.screenWidth*(0.55), self.screenHeight*(0.75)))
        platform16 = Platform(self.screenWidth*0.65,self.screenHeight*0.62, "platforms/Untitled__6.png")
        platform17 = Platform(self.screenWidth*0.5,self.screenHeight*0.62, "platforms/Untitled__6.png")
        platform18 = Platform(self.screenWidth*0.7,self.screenHeight*0.15, "platforms/Untitled__9.png")
        
        #add other platforms later
        #add cooordinates and image path later once i get the actually platforms
        
        self.platforms.add(platform1)
        self.platforms.add(platform2)
        self.platforms.add(platform3)
        self.platforms.add(platform4)
        self.platforms.add(platform5)
        self.platforms.add(platform6)
        self.platforms.add(platform7)
        self.platforms.add(platform8)
        self.platforms.add(platform9)
        self.platforms.add(platform10)
        self.platforms.add(platform11)
        self.platforms.add(platform12)
        self.platforms.add(platform13)
        self.platforms.add(platform14)
        self.platforms.add(platform15)
        self.platforms.add(platform16)
        self.platforms.add(platform17)
        self.platforms.add(platform18)
        
        self.clock = pygame.time.Clock()
        
        #upload acid drip
        acid_drip = AcidDrip(self.screenWidth*(0.84),self.screenHeight*(0.53))
        
        self.AcidDrips.add(acid_drip)
        
        #upload jems
        jem1 = Jems(0,self.screenHeight*0.02)
        jem2 = Jems(self.screenWidth*(0.95),self.screenHeight*(0.6))
        
        self.JemsList.add(jem1)
        self.JemsList.add(jem2)
        
        #levers
        lever1 = Lever(self.screenWidth*0.3,self.screenHeight*0.535)
        self.LeverList.add(lever1)
        
        #doors
        door = Door(self.screenWidth*0.95, 0)
        door.image = pygame.transform.scale(door.image, (door.image.get_width()*0.8, door.image.get_height()*0.9))
        door.rect = door.image.get_rect(topleft = (self.screenWidth*0.95, 0))
        self.Doors.add(door)
        
        #player
        self.player.rect.x= 0
        self.player.rect.y=self.screenHeight*(0.74)
    
        
        #refresh
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
          
         
        
        
    def draw(self, screen):
        print(self.player.highjump)
        self.get_conditionals()
        self.player.update()
        self.refresh.append(self.player.rect)
        
        screen.blit(self.background,(0,0))
        screen.blit(self.player.image, self.player.rect)
        self.platforms.draw(screen)
        self.AcidDrips.draw(screen)
        self.JemsList.draw(screen)
        self.LeverList.draw(screen)
        self.Doors.draw(screen)
        
        
    
    def get_event(self, event):
        
        keys = pygame.key.get_pressed()
                
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
            
        #lever switching
        collisionLever=pygame.sprite.spritecollideany(self.player,self.LeverList)
        if(collisionLever != None):
            collisionLever.switch() 
            
        else:
            for i in self.LeverList:
                self.refresh.append(i.rect)
                
        #checking for jem collision
        collisionJemItem=pygame.sprite.spritecollideany(self.player, self.JemsList)
        if(collisionJemItem!=None):
            collisionJemItem.kill()
            gemCollection = pygame.mixer.Sound("Sounds/reward.wav") # defines the sound
            pygame.mixer.Sound.play(gemCollection) 
            self.player.increaseJem(1)
            self.jems=self.player.jems
            print(self.player.jems)
        else:
            for i in self.JemsList:
                self.refresh.append(i.rect)
        
        #doors collision
        collisionDoor = pygame.sprite.spritecollideany(self.player, self.Doors)
        if(collisionDoor != None):
            print("finished stage")
            self.clock.tick()
            self.player.time=self.clock.get_time()/1000
            
           
            self.done=True
            self.next_state="FinishPage"
        
            self.player.rect.x=0
            self.player.rect.y=self.screenHeight*0.74
            pygame.mixer.pause() # stops all sounds  
            finishPageSound = pygame.mixer.Sound("Sounds/frKitchenSoundtrack.wav") # defines the sound
            pygame.mixer.Sound.play(finishPageSound,-1)   
        else:
            for i in self.Doors:
                self.refresh.append(i.rect)
            
        #checking for acid collision
        collisionAcid = pygame.sprite.spritecollideany(self.player, self.AcidDrips)
        if(collisionAcid != None):
            print("player has been killed")
            pygame.mixer.pause()
            acidDripSound = pygame.mixer.Sound("Sounds/acid.wav") # defines the sound
            pygame.mixer.Sound.play(acidDripSound)
            self.done=True
            self.next_state="MainPage"
            mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
            pygame.mixer.Sound.play(mainPageSound,-1) 
            #pygame.mixer.Sound.stop(self.sewerSound)
            #pygame.mixer.Sound.play(self.mainPageSound)
            self.player.rect.x=0
            self.player.rect.y=self.screenHeight*0.74

            #pygame.quit()
            #sys.exit()
            #main = False
        else:
            for i in self.AcidDrips:
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
            mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
            pygame.mixer.Sound.play(mainPageSound,-1) 
            #pygame.mixer.Sound.stop(self.sewerSound)
            #pygame.mixer.Sound.play(self.mainPageSound)
            
        
    def get_conditionals(self):
        
        self.refresh = []
        #lever making platforms
        collisionLever=pygame.sprite.spritecollideany(self.player,self.LeverList)
        for i in self.LeverList:
            if(i==collisionLever):
                i.on==True
            if(i.on == True and len(self.platforms) == 18):
                platform19 = Platform(self.screenWidth*0.2, self.screenHeight*0.53, "platforms/Untitled__3.png")
                platform20 = Platform(self.screenWidth*0.1,self.screenHeight*0.47, "platforms/Untitled__3.png")
                platform21 = Platform(self.screenWidth*0.02,self.screenHeight*0.41, "platforms/Untitled__3.png")
                platform22 = Platform(self.screenWidth*0.15,self.screenHeight*0.35, "platforms/Untitled__3.png")
                platform23 = Platform(self.screenWidth*0.25,self.screenHeight*0.28, "platforms/Untitled__3.png")
                platform24 = Platform(self.screenWidth*0.1,self.screenHeight*0.15, "platforms/Untitled__3.png")
                self.platforms.add(platform19)
                self.platforms.add(platform20)
                self.platforms.add(platform21)
                self.platforms.add(platform22)
                self.platforms.add(platform23)
                self.platforms.add(platform24)
                
        if(self.player.inAir==True):
            if(self.player.rect.y<self.screenHeight)-10:
                self.player.gravity()
            self.refresh.append(self.player.rect)

        if(self.player.rect.y>self.screenHeight-10):
            self.player.inAir=False
            self.player.rect.clamp_ip(self.screen_rect)
            self.refresh.append(self.player.rect)
        #testing to see if player hit bottom of screen
        if(self.player.rect.y == self.screenHeight-61):
            print("The player has fallen down")
            self.done=True
            self.next_state="MainPage"
             
            pygame.mixer.pause() # stops all sounds  
            mainPageSound = pygame.mixer.Sound("Sounds/mainPage.wav") # defines the sound
            pygame.mixer.Sound.play(mainPageSound,-1) 
            #pygame.mixer.Sound.stop(self.sewerSound)
            self.player.rect.x=0
            self.player.rect.y=self.screenHeight*0.74
            #pygame.mixer.Sound.play(self.mainPageSound)
            #pygame.quit()
            #sys.exit()
            main = False
        
        #acid drop
        for i in self.AcidDrips:
            if i.rect.y >= self.screenHeight*0.7:
                i.rect.y = self.screenHeight*(0.53)
                self.refresh.append(i.rect)
            i.moveDown(1)
            i.update()
            self.refresh.append(i.rect)
        
        #platform collision
        collisionPlatform = pygame.sprite.spritecollideany(self.player,self.platforms)
        if(collisionPlatform != None):
            if(self.player.rect.bottom > collisionPlatform.rect.top and self.player.rect.bottom < collisionPlatform.rect.bottom):
                self.player.inAir=False
            if(self.player.rect.top < collisionPlatform.rect.bottom and self.player.rect.bottom > collisionPlatform.rect.bottom):
                self.player.inAir=True
        else:
            self.player.inAir = True
            
        
            

            
        
                
        
        
        
        
        
