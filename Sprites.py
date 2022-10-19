##Rayna Hata 
#January 2022
#Sprite class
# Will hold the sprites


from socketserver import ThreadingUDPServer
import sys
import os
import pygame
  

class Player(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super().__init__()

        self.images=[] #array holding the different image walk sequence 
        self.images.append(pygame.image.load("RatWalk/ratwalk1.png").convert_alpha())
        self.images.append(pygame.image.load("RatWalk/ratwalk2.png").convert_alpha())
        self.images.append(pygame.image.load("RatWalk/ratwalk3.png").convert_alpha())
        self.index=0 #what index we are on 
        self.image=self.images[self.index]
        self.direction=True #seeing if the direction of the sprite is the same as the previouss 
        self.rect = self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        self.changex = 0 # value to move along x
        self.changey=0
        self.previousLRKey=' '
        self.alive=True
        self.jems=3
        self.Hearts=1 #when starting a new game, create a local variable called hearts and DO NOT change self.hearts or else upgrade will go away 
        self.inAir=False
        self.newDirection='left'
        self.direction='left'
        self.speed=1
        self.highjump=1
        self.time=0

    
   
    def increaseSpeed(self):
        self.speed+=1
    
    def increaseJump(self):
        self.highjump+=1

    def getPlayerPos(self):
        return self.rect

    #self.previousKey=='w' or self.previousKey=='s'  or 
    def move_left(self, move_x):
        

        self.newDirection='left'
        self.changex=-move_x*self.speed
        self.previousLRKey='a'


    def gravity(self):
        
        self.changey+=3
        
    def move_right(self, move_x):
        '''move player right'''
        
    
        self.newDirection='right'
        self.changex=move_x*self.speed
        self.previousLRKey='d'

    

    def move_up(self, move_y):
        '''move player up'''
        
        self.changey = -move_y*self.highjump
        self.inAir=True
        self.newDirection='up'
 
    def update(self):
        '''update player movement'''
        self.index+=1
        if self.index>=len(self.images):
            self.index=0
        
        
        if self.newDirection != 'up' and self.newDirection != self.direction:
            for i in range (len(self.images)):
                self.images[i]=pygame.transform.flip(self.images[i],True,False)
            self.direction = self.newDirection # keep track of whether the images are facing left or right
        
        
        
        self.image=self.images[self.index]
            
        self.rect.x += self.changex
        self.rect.y += self.changey
        self.changex=0
        self.changey=0
        

    def increaseHeart(self):
        self.Hearts+=1

       

    #increase jem when jem is found, time is cleared etc. 
    def increaseJem(self,number):
        self.jems+=number

    #decrease jem, subtract when upgrade bought 
    def decreaseJem(self,number):
        self.jems-=number


    def collided(self,location):
        return self.rect.colliderect(location)




    


    

    
class Jems(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.image = pygame.image.load("jems.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        

    
    def update(self,xloc,yloc):
        self.rect.x=xloc
        self.rect.y=yloc
        return  

class AcidDrip(pygame.sprite.Sprite):

    #initiliaze class
    def __init__(self,xpos,ypos):
        super().__init__()
        #initialize image
        self.image = pygame.image.load("obstacles/aciddrip.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.3,self.image.get_height()*0.3)) 
        #draw rect around image
        self.rect = self.image.get_rect()
        #set positions for x and y of image
        self.rect.x = xpos
        self.rect.y = ypos
        #set the change in y position of class
        self.change_y = 0
    
    #return position of rect
    def getPos(self):
        return self.rect
    
    #set the change in y of class
    def moveDown(self, move_y):
        self.change_y = move_y
    
    #updates position of class
    def update(self):
        self.rect.y += self.change_y
        self.change_y = 0
#sword 
#spikes
class Spikes(pygame.sprite.Sprite):

    #initiliaze class
    def __init__(self,xpos,ypos):
        super().__init__()
        #initialize image
        self.image = pygame.image.load("obstacles/spikes.png").convert_alpha()
        #draw rect around image
        self.rect = self.image.get_rect()
        #set positions for x and y of image
        self.rect.x = xpos
        self.rect.y = ypos
        #set the change in y position of class
        self.change_y = 0
    
    #return position of rect
    def getPos(self):
        return self.rect
    
#lever class 
class Platform(pygame.sprite.Sprite):

    def __init__(self,xpos,ypos,image_path):
        #bring in super class of sprite
        super().__init__()
        #draw in image based on specfied image path
        self.image = pygame.image.load(image_path).convert_alpha()
        #get rect around image
        self.rect = self.image.get_rect()
        #provide x for rect
        self.rect.x = xpos
        #provide y for rect
        self.rect.y = ypos
    
    
    def collision(self,character):
        return self.rect.colliderect(self,character)

#MainPageSprties
class MainPageSprites(pygame.sprite.Sprite):

    def __init__(self,name,xpos,ypos,scale,image_path):
        #bring in super class of sprite
        super().__init__()
        #draw in image based on specfied image path
        self.image = pygame.image.load(image_path)
        self.image=pygame.transform.scale(self.image,(self.image.get_width()*scale,self.image.get_height()*scale))
        self.name=name
    
        #self.image=self.image.subsurface(300,300)
        #get rect around image
        self.rect = self.image.get_rect()
       

        #provide x for rect
        self.rect.x = xpos
        #provide y for rect
        self.rect.y = ypos
        self.unlocked=False
    
    
    def collision(self,character):
        return self.rect.colliderect(self,character)

        
 
class InfoPageSprites(pygame.sprite.Sprite):
     def __init__(self,name,xpos,ypos,scale,image_path):
        #bring in super class of sprite
        super().__init__()
        #draw in image based on specfied image path
        self.image = pygame.image.load(image_path)
        self.image=pygame.transform.scale(self.image,(self.image.get_width()*scale,self.image.get_height()*scale))
        self.name=name
    
        #self.image=self.image.subsurface(300,300)
        #get rect around image
        self.rect = self.image.get_rect()
       

        #provide x for rect
        self.rect.x = xpos
        #provide y for rect
        self.rect.y = ypos


class UpgradesPageSprites(pygame.sprite.Sprite):
    def __init__(self,name,xpos,ypos,scale,image_path):
        #bring in super class of sprite
        super().__init__()
        #draw in image based on specfied image path
        self.image = pygame.image.load(image_path)
        self.image=pygame.transform.scale(self.image,(self.image.get_width()*scale,self.image.get_height()*scale))
        self.name=name
    
        #self.image=self.image.subsurface(300,300)
        #get rect around image
        self.rect = self.image.get_rect()
       

        #provide x for rect
        self.rect.x = xpos
        #provide y for rect
        self.rect.y = ypos

class Lever(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.image = pygame.image.load("obstacles/leverclosed.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.on = False
        
    def switch(self):
        if(self.on == False):
            self.image = pygame.image.load("obstacles/leverOpen.png").convert_alpha()
            self.on = True
        
        

class Door(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.image = pygame.image.load("obstacles/door.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        
class Knife(pygame.sprite.Sprite):

    #initiliaze class
    def __init__(self,xpos,ypos):
        super().__init__()
        #initialize image
        self.image = pygame.image.load("obstacles/knife.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*0.07, self.image.get_height()*0.07))
        #draw rect around image
        self.rect = self.image.get_rect()
        #set positions for x and y of image
        self.rect.x = xpos
        self.rect.y = ypos
        #set the change in y position of class
        self.change_y = 0
    
    #return position of rect
    def getPos(self):
        return self.rect
      
class Foot(pygame.sprite.Sprite):
    #initiliaze class
    def __init__(self,xpos,ypos):
        super().__init__()
        #initialize image
        self.image = pygame.image.load("obstacles/foot.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.1,self.image.get_height()*0.1)) 
        #draw rect around image
        self.rect = self.image.get_rect()
        #set positions for x and y of image
        self.rect.x = xpos
        self.rect.y = ypos
        #set the change in y position of class
        self.change_y = 0
    
    #return position of rect
    def getPos(self):
        return self.rect
    
    #set the change in y of class
    def moveDown(self, move_y):
        self.change_y = move_y
    
    #updates position of class
    def update(self):
        self.rect.y += self.change_y
        self.change_y = 0
        
class Cheese(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.image = pygame.image.load("obstacles/cheese.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.2,self.image.get_height()*0.2))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class FinishPageSprites(pygame.sprite.Sprite):
    def __init__(self,name,xpos,ypos,scale,image_path):
        #bring in super class of sprite
        super().__init__()
        #draw in image based on specfied image path
        self.image = pygame.image.load(image_path)
        self.image=pygame.transform.scale(self.image,(self.image.get_width()*scale,self.image.get_height()*scale))
        self.name=name
    
        #self.image=self.image.subsurface(300,300)
        #get rect around image
        self.rect = self.image.get_rect()
       

        #provide x for rect
        self.rect.x = xpos
        #provide y for rect
        self.rect.y = ypos
