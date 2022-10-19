#Rayna Hata 
#January 2022
#Moving Objects 
# Imports the rat and then make it move 


import sys
import pygame

from Sprites import *


#initialized the game 
pygame.init()

# initialize the fonts
try:
    pygame.font.init()
except:
    print ("Fonts unavailable")
    sys.exit()




# create a game clock

gameClock = pygame.time.Clock()

# create a screen (width, height)
screen = pygame.display.set_mode( (0,0), pygame.FULLSCREEN)
screenHeight=screen.get_rect().height
screenWidth=screen.get_rect().width

#sets the background full screen
background=pygame.image.load('background.png',)
background= pygame.transform.scale(background,(screenWidth,screenHeight)) 






# List that contains all sprites in the gamel; useful in scenes with muliple objects 
currentSpriteList = pygame.sprite.Group()
currentJemList=pygame.sprite.Group()
#import the player

player = Player(0,(screenHeight-50))


screen.blit(player.image,(player.getPlayerPos()))
print(player.rect)

print(player.rect.width)
print(player.rect.height)


jems1=Jems(120,40)
currentJemList.add(jems1)
jems2=Jems(400,40)
currentJemList.add(jems2)
jems3=Jems(600,40)
currentJemList.add(jems3)
#currentSpriteList.add(player) #adding in the current player 
currentSpriteList.add(player)





#fill the screen with white 
#screen.fill( (255, 255, 255) )
screen.blit(background,(0,0))
currentSpriteList.draw(screen)
currentJemList.draw(screen)

#screen.blit(player.image, player.rect)
#screen.blit(jems.image,jems.rect)  #placing a jem at this point 




# update the screen
pygame.display.update()


####################### Main Event Loop #########################
# moving the rat using the WASD keys 


refresh = []

previousKey= ' '
playerStepLength=screenWidth/30#player step distance

playerJumpLength=screenHeight/20

#pygame.display.update()
#player.rect = pygame.Rect( player.rect.x,player.rect.y, player.rect.width, player.rect.height  )
#jems.rect=pygame.Rect(jems.rect.x,jems.rect.y,jems.rect.width,jems.rect.height)





print ("Entering main loop")
while 1:

    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():

        
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        
        if keys[pygame.K_a]:
            print('left')
           
            if(player.rect.x>=0 and player.rect.x<screenWidth):
                player.move_left(playerStepLength)
              
            else:
                player.rect.clamp_ip(screen.get_rect())
                
            
           #checking for collision
            collisionItem=pygame.sprite.spritecollideany(player, currentJemList)
            if(collisionItem!=None):
                collisionItem.kill()
                player.increaseJem(1)
            else:
                for i in currentJemList:
                    refresh.append(i.rect)
            
            refresh.append(player.rect)
            

        if keys[pygame.K_d]:
            print('right')
           
            if(player.rect.x>=0 and player.rect.x<(screenWidth-player.rect.width)):
                player.move_right(playerStepLength)
                
            else:
                player.rect.clamp_ip(screen.get_rect())
                
            collisionItem=pygame.sprite.spritecollideany(player, currentJemList)
            if(collisionItem!=None):
                collisionItem.kill()
                player.increaseJem(1)
            else:
                for i in currentJemList:
                    refresh.append(i.rect)
            
        
            refresh.append(player.rect)
             

        if keys[pygame.K_w]:
            print('jump')

            if(player.rect.y>=0 and player.rect.y<screenHeight):
                player.move_up(playerJumpLength)
                
            else:
                player.rect.clamp_ip(screen.get_rect()) #keeping the rat within the border of the screen rect 
           
            collisionItem=pygame.sprite.spritecollideany(player, currentJemList)
            if(collisionItem!=None):
                collisionItem.kill()
                player.increaseJem(1)
            else:
                for i in currentJemList:
                    refresh.append(i.rect)
            
            refresh.append(player.rect)
            

         #game ending condition 
        if keys[pygame.K_q]:
            print("Game has been quit. Thanks for playing!")
            print(player.jems)
        
            pygame.quit()
            sys.exit()
            main = False  

        
        
    if(player.inAir==True):
        if(player.rect.y<screenHeight)-10:
            player.gravity()
        refresh.append(player.rect)

    if(player.rect.y>screenHeight-10):
        player.inAir=False
        player.rect.clamp_ip(screen.get_rect())
        refresh.append(player.rect)
   
    #Draw sprites at once all/refresh the position of the player
    
    # player update
    
    
    # screen redrawing code

    player.update()
    refresh.append(player.rect)
    screen.blit(background,(0,0))
    screen.blit(player.image, player.rect)
    currentSpriteList.draw(screen)
    currentJemList.draw(screen)
    
    
    

    pygame.display.update() # update screen

    refresh = []
    gameClock.tick(30)

   
        
# done
print ("Terminating")