import pygame
import random
import time
import sys

pygame.init() # initializing pygame 

# Setting variables for the game
WIDTH , LENGHT =  400,600
screen = pygame.display.set_mode((WIDTH , LENGHT))
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 90
SPEED = 5

SCORE = 0
COIN_SCORE = 0
# Set the caption
pygame.display.set_caption("CAR")
# Loading the coin image 
coin = pygame.image.load('coin.png')
coin = pygame.transform.scale(coin , (70,70))


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
 
      def move(self): # method responsible for moving enemy car
        global SCORE
        self.rect.move_ip(0,10)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(50, 380), 0)
 
      def draw(self, surface): # blitting on the screen
        screen.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
        
 
    def move(self):# method responsible for moving player's car
        pressed = pygame.key.get_pressed()
        if self.rect.left > 40:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 40:        
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        # checking for collecting coins
        coins_collected = pygame.sprite.spritecollide(self, bonus, True)
        if coins_collected:
            global COIN_SCORE
            COIN_SCORE += 1
         

 
    def draw(self, screen): 
        # blitting on the screen
        screen.blit(self.image, self.rect)
        
        
class Coin(pygame.sprite.Sprite):
      def __init__(self , screen ,coin):
        super().__init__() 
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
        
       
 
      def move(self): # motion of the coin
        self.rect.move_ip(0,3)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 380), 0)
        

      def draw(self): # blitting on the screen
        screen.blit(self.image, self.rect)
        
        

# variables for the calsses
P1 = Player()
E1 = Enemy()
C = Coin(screen , coin)
# adding sprites to groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)

bonus = pygame.sprite.Group()
bonus.add(C)

# creating an userevent for coin
ADD_COIN = pygame.USEREVENT + 3
pygame.time.set_timer(ADD_COIN, 3000)




background_road = pygame.image.load('AnimatedStreet.png')
# font settings
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

game_sound = True
play_sound = pygame.mixer.Sound('game_sound.wav').play(-1)
cnt =0
while True: # main loop
    for event in pygame.event.get():
        # event for quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # for collecting the coin
        elif event.type == ADD_COIN:
            new = Coin(screen,coin)
            all_sprites.add(new)
            bonus.add(new)
    
    if game_sound: 
        if pygame.sprite.spritecollideany(P1, enemies): # if player's car colliding with the enemy car, stop the game
            play_sound.stop()
            pygame.mixer.Sound('crash.mp3').play()
            time.sleep(3)
            screen.fill(RED)
            screen.blit(game_over, (30,250))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

 


     # blitting on the screen score and coin_score     
    screen.blit(background_road, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render(str(COIN_SCORE), True , GREEN)
    screen.blit(scores, (10,10))
    screen.blit(coin_scores , (370,10))  

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
     
          
    pygame.display.update()
    clock.tick(60)
    