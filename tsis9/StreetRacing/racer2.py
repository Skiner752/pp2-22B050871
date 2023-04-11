import pygame
import random
import time
import sys
# initialization
pygame.init()
# standart variables for the game
WIDTH , LENGHT =  400,600
screen = pygame.display.set_mode((WIDTH , LENGHT))
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60
SPEED = 5
E_SPEED = 7
SCORE = 0
COIN_SCORE = 0
# caption
pygame.display.set_caption("CAR")
# loading and transforming coin images
coin = pygame.image.load('coin.png')
coin = pygame.transform.scale(coin , (70,70))
bit = pygame.image.load('bit.png')
bit = pygame.transform.scale(bit , (70,70))
ton = pygame.image.load('ton.png')
ton = pygame.transform.scale(ton , (70,70))
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
 
      def move(self): #method responsible for moving the enemy car
        global SCORE
        if COIN_SCORE <=5 :
            self.rect.move_ip(0,E_SPEED)
        if COIN_SCORE >=6  :
            self.rect.move_ip(0, E_SPEED + 1.5)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 380), 0)
 
      def draw(self, surface): # blitting on the screen
        screen.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
        
 
    def move(self): # method for controling car
        global COIN_SCORE
        pressed = pygame.key.get_pressed()
        if self.rect.left > 40:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 40:        
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
          

 
    def draw(self, screen):
        if self in coins:
            screen.blit(self.image, self.rect)
        
        

class Coin(pygame.sprite.Sprite):
      def __init__(self ,coin):
        super().__init__() 
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
        
       
 
      def move(self): # moving the coin
        self.rect.move_ip(0,4)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 380), 0)
        

      def draw(self): # blitting coin on the screen 
        screen.blit(self.image, self.rect)
        
class Bitcoin(pygame.sprite.Sprite): # another bonus coin
    def __init__(self , bit):
        super().__init__()
        self.image = bit
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,380),0)       
    
    def move(self):
        self.rect.move_ip(0,2)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,380) , 0)
    
    def draw(self):
        screen.blit(self.image , self.rect)

class Toncoin(pygame.sprite.Sprite): # loss coin
    def __init__(self , ton):
        super().__init__()
        self.image = ton
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,380),0)       
    
    def move(self):
        self.rect.move_ip(0,3)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,380) , 0)
    
    def draw(self):
        screen.blit(self.image , self.rect)
# Instances of classes
P1 = Player()
E1 = Enemy()
C = Coin(coin)
B = Bitcoin(bit)
T = Toncoin(ton)
# Creating enemy group
enemies = pygame.sprite.Group()
enemies.add(E1)
# Group for all sprites 
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
all_sprites.add(T)
all_sprites.add(B)
# bonus 1 , bonus2 and loss groups
bonus1 = pygame.sprite.Group()
bonus1.add(C)

bonus2 = pygame.sprite.Group()
bonus2.add(B)

loss = pygame.sprite.Group()
loss.add(T)
# loading backgroung image
background_road = pygame.image.load('AnimatedStreet.png')
# Setteng Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

game_sound = True
# playing music sound inf.
play_sound = pygame.mixer.Sound('game_sound.wav').play(-1)



while True: # main game loop
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT: # quitting the game
            pygame.quit()
            sys.exit()


    
    if game_sound: 
        if pygame.sprite.spritecollideany(P1, enemies): # If player collides with enemy
            play_sound.stop()
            pygame.mixer.Sound('crash.mp3').play()
            time.sleep(3)
            screen.fill(RED)
            screen.blit(game_over, (WIDTH / 2 -150 , LENGHT / 2 - 30))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        elif pygame.sprite.spritecollide(P1 , bonus1 , True): # If player collides with bonus1
            COIN_SCORE += 1
            new = Coin(coin)
            all_sprites.add(new)
            bonus1.add(new)
            
        

        elif pygame.sprite.spritecollide(P1 , bonus2 , True): # If player collides with bonus2
            COIN_SCORE += 2
            new = Bitcoin(bit)
            all_sprites.add(new)
            bonus2.add(new)
            
        elif pygame.sprite.spritecollide(P1 , loss , True): # If player collides with loss
            COIN_SCORE -= 2
            new = Toncoin(ton)
            all_sprites.add(new)
            loss.add(new)
            if COIN_SCORE <= 0:
                play_sound.stop()
                time.sleep(3)
                screen.fill(RED)
                screen.blit(game_over, (30,250))
                pygame.display.update()
                for entity in all_sprites:
                    entity.kill()
                time.sleep(2)
                pygame.quit()
                sys.exit()

    # screen blitting score and coin_score
    screen.blit(background_road, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render(str(COIN_SCORE), True , GREEN)
    screen.blit(scores, (10,10))
    screen.blit(coin_scores , (370,10))  

    for entity in all_sprites: # for blitting all sprites from group
        screen.blit(entity.image, entity.rect)
        entity.move()
    
     
    pygame.display.update()
    clock.tick(FPS)
    