# !!!!!  THIS IS THE STARTING TEMPLATE FOR THE ENGINEERING EXPO DEMONSTRATION ONLY  !!!!
# !!!!!  REFER TO MAIN.PY FOR THE COMPLETE CODE !!!!!

import pygame, sys
from pygame.locals import *
from random import randint

WIN_WIDTH = 800
WIN_HEIGHT = 630
BACKGROUND_COL = (0,0,0)

TOP_B = 150 
RIGHT_B = WIN_WIDTH 
LEFT_B = 0 
BOTTOM_B = WIN_HEIGHT 

FPS = 60

def message(text_image, screen):
    text = pygame.image.load(text_image)
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

class Ball():
    def __init__(self, x_dis, y_dis, image, y_pos, x_pos=0):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.hit_border = False
        self.x_dis, self.y_dis = x_dis, y_dis

    def move(self):
        self.rect.move_ip(self.x_dis, self.y_dis) 
        if (self.rect.bottom >= BOTTOM_B or self.rect.top <= TOP_B or self.rect.right >= RIGHT_B or self.rect.left <= LEFT_B) and self.hit_border == False:
            self.hit_border = True
        if self.hit_border == True:
            if self.rect.bottom >= BOTTOM_B:
                self.y_dis = -(self.y_dis)
            if self.rect.top <= 0:
                self.y_dis = -(self.y_dis)
            if self.rect.right >= RIGHT_B:
                self.x_dis = -(self.x_dis)
            if self.rect.left <= LEFT_B:
                self.x_dis = -(self.x_dis)   
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player():
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_WIDTH/2, -50)
        self.no_grav = False
    # !!!!!!  PLAYER MOVE FUNCTION    !!!!!!!!!!!!!!!!!
    def move(self, splat):
        if splat == False:
            key = pygame.key.get_pressed()             
            if key[K_UP] and self.rect.top >= 0:
                self.rect.move_ip(0,-12)
            if key[K_LEFT] and self.rect.left>=LEFT_B:
                self.rect.move_ip(-7,0)
            if key[K_RIGHT] and self.rect.right<=RIGHT_B:
                self.rect.move_ip(7,0) 
                 
            if self.rect.bottom >= BOTTOM_B:
                self.no_grav = True 
            elif self.rect.top <= 0:
                self.no_grav = False     

    def gravity(self):
            if self.no_grav == False:
                self.rect.move_ip(0,5)
            else:
                self.rect.move_ip(0,-5)
            
    def collision(self, obstacles):
        if self.rect.collidelist(obstacles) != -1:  
            return True       
           
    def draw(self, screen):
        screen.blit(self.image, self.rect)

ball1 = Ball(5, 5, "graphics/pink_ball.png", randint(TOP_B, BOTTOM_B), randint(0, WIN_WIDTH))   
ball2 = Ball(5, 5, "graphics/pink_ball.png", randint(TOP_B, BOTTOM_B), randint(0, WIN_WIDTH))   
ball3 = Ball(5, 5, "graphics/pink_ball.png", randint(TOP_B, BOTTOM_B), randint(0, WIN_WIDTH)) 
ball4 = Ball(5, 5, "graphics/pink_ball.png", randint(TOP_B, BOTTOM_B), randint(0, WIN_WIDTH)) 

balls = [ball1, ball2, ball3, ball4] 

player = Player("graphics/green_ball.png") 
       
def main():
    pygame.init()

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Bouncy Ballz")
    window.fill(BACKGROUND_COL)  

    clock = pygame.time.Clock() 

    game_over = False
    splat = False

    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
                sys.exit()

        if game_over == False:

            #APPLY GRAVITY
            player.gravity()
            
            #MOVE BOUNCY BALLS
            for ball in balls:
                ball.move()

            #MOVE PLAYER 
            player.move(splat)  

            #COLLISION
            player.collision(balls)
            if player.collision(balls) == True:
                player.image = pygame.image.load("graphics/splat.png")
                splat = True
                game_over = True
               

            window.fill(BACKGROUND_COL)

            #DRAW BOUNCY BALLS
            for ball in balls:
                ball.draw(window)
            

            #DRAW PLAYER
            player.draw(window)

            pygame.display.flip() 
            clock.tick(FPS) 
        else:
            
            # !!!!!!GAME OVER SCREEN !!!!!!!!1

            window.fill(BACKGROUND_COL)
            player.image = pygame.image.load("graphics/splat.png")
            player.draw(window)
            message("graphics/game_over.png", window)
            pygame.display.flip()
      
           

if __name__ == "__main__":
    main()