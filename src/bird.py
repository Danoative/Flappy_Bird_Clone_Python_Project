# Create a Bird class
import pygame
import os
#import main

class FlappyBird(pygame.sprite.Sprite):
    #still have to add image and sound into init
    
    #DECLARE VARIABLE   
    x = None
    y = None
    img_string = None
        
    #CONSTRUCOTRS
    def __init__(self, x, y): #, img_string
        # Initialize attributes for the bird
        pygame.sprite.Sprite.__init__(self)
        
        #Bird (Initial) lOcation
        self.x = x  
        self.y = y 
        
        #self.img_string = img_string
        
        #Bird movement attribute
        self.Y_velocity = -200
        self.gravity = 1
        
        #self.sound[collide]
        
        #adding image
        cwd = os.path.dirname(__file__)
        self.img = pygame.image.load(os.path.join(cwd, "img", "plane.png"))
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
        
    def flap(self):
        # Implement the bird's jump action
        print("the bird is flapping")
        self.rect.y += self.Y_velocity
        

    def update(self,screen_height):
        # Implement the bird's movement (gravity + horizontal)
        self.rect.y += self.gravity
        print("current y position: seft.rect.y: " + str(self.rect.y))
        # also limit to not allow bitd move out of the screen (vertically)
        if self.rect.top < 0:
            self.rect.top = 0
            #we could possible kill the bird or just not allow them to not go pass the border
                #self.Y_velocity = 0
                #self.gravity =  0
            # we chosse the second one here
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height