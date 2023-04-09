import random
import sys
import pygame
import time

pygame.init() # initializing pygame
# setting standart variables for the game
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW =  (255, 255, 0, 255)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19, 255)
DARK_GREEN = (0, 100, 0, 255)
BLOCK_SIZE = 40
clock = pygame.time.Clock()
LEVEL = 1 
SCORE = 0
font_small = pygame.font.SysFont("Verdana", 20)

class Point: # taking the coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Level:
    def __init__(self,x ,y):
        self.location = Point(x,y)
    def level1(self): # creating the bush 
        pygame.draw.rect(screen,DARK_GREEN,(self.location.x * BLOCK_SIZE,self.location.y * BLOCK_SIZE, 9*BLOCK_SIZE,8*BLOCK_SIZE))
    

class Snake:
    def __init__(self): # snake's body parameters 
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE //2 ,
                y=HEIGHT // BLOCK_SIZE //2 ,
            ),
        ]
        
    def draw_body(self):
        for body in self.body[1:]: # drawing the body without head
            pygame.draw.rect(screen,BLUE,(body.x * BLOCK_SIZE ,body.y * BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))
    
    def draw_head(self): # drawing head
        head = self.body[0]
        pygame.draw.rect(screen , RED , (head.x * BLOCK_SIZE, head.y * BLOCK_SIZE , BLOCK_SIZE , BLOCK_SIZE))
    
    def move(self, dx, dy, game_over ,screen):
    # Get the current head position
        head = self.body[0]
    
    # Calculate the new head position
        new_head = Point(head.x + dx, head.y + dy)
    
    # Check if the new head position collides with the body
        if any(part.x == new_head.x and part.y == new_head.y for part in self.body[1:]):
            white_surface = pygame.Surface((WIDTH, HEIGHT))
            white_surface.fill(WHITE)
            screen.blit(white_surface, (0, 0))
            screen.blit(game_over, (160,400))
            pygame.display.update()
            pygame.mixer.Sound('game_over.mp3').play()
            time.sleep(3)
            pygame.quit()
            sys.exit()
            
    
    # Move the body parts
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        
    # Move the head to the new position
        self.body[0] = new_head
    
    # Apply the border constraints
        self.border()

       
    def check_collision(self, food): # checking whether snake 'eats' food
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        
        return True
             
    def check_collision_wall(self,wall):# checking whether snake collides with the screen's boarder
        if wall.location.x != self.body[0].x: 
            return False
        if wall.location.y != self.body[0].y:
            return False
        
        return True
    
    
    
    def border(self): # if thw snake leaves playing area
        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0
        
       


def draw_grid(): # white stripes
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


        



class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self): # drawing apple 
        pygame.draw.rect(screen,GREEN,(self.location.x * BLOCK_SIZE,self.location.y * BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))

    def generator(self , S): # randomly appearing apples
        while True:
            x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
            y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)
            if not any(part.x == x and part.y == y for part in S.body):
                self.location = Point(x, y)
                break

class Poison:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):# drawing poison
        pygame.draw.rect(screen,YELLOW,(self.location.x * BLOCK_SIZE,self.location.y * BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))

    def generator(self , S):# randomly appearing poison
        while True:
            x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
            y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)
            if not any(part.x == x and part.y == y for part in S.body):
                self.location = Point(x, y)
                break


def main():
    # variables for the calsses
    S = Snake()
    F = Food(5, 5)
    L = Level(10,10)
    P = Poison(15,15)
    # motion
    dx, dy = 0, -1
    ok = True
    FPS = 5 
    check = True
    direction = 'up'
    #setting fonts
    font =  pygame.font.SysFont("Verdana", 90)
    game_over = font.render("Game Over", True, BLACK)
    # counters
    global SCORE , LEVEL
    LEVEL = 1 
    SCORE = 0
    
    while not done:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True # exit game
            if event.type == pygame.KEYDOWN:
                # motion of the snake
                if event.key == pygame.K_UP and direction != 'down':
                    dx, dy = 0, -1
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up' :
                    dx, dy = 0, +1
                    direction = 'down'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    dx, dy = 1, 0
                    direction = 'right'
                elif event.key == pygame.K_LEFT and direction != 'right':
                    dx, dy = -1, 0
                    direction = 'left'
            
                if event.key == pygame.K_p:
                    LEVEL = 2   
        S.move(dx, dy , game_over , screen)
        # If snake collect food
        if S.check_collision(F):
            pygame.mixer.Sound('collected_coin.mp3').play()
            SCORE += 1
            if SCORE % 5 == 0 and SCORE != 0:
                LEVEL += 1
                ok = True
                
            S.body.append(
                Point(S.body[1].x, S.body[1].y)
            )
            F.generator(S)
            
        if S.check_collision(P): # If snake collect poison
            
            
            if len(S.body) == 2:
                white_surface = pygame.Surface((WIDTH, HEIGHT))
                white_surface.fill(WHITE)
                screen.blit(white_surface, (0, 0))
                pygame.mixer.Sound('small-coughing.mp3').play()
                screen.blit(game_over, (160,400))
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                sys.exit()
                
            S.body.pop()

            P.generator(S)
        # increasing the speed of snake 
        if LEVEL > 1 and ok == True:
            FPS += 2
            ok = False
            
        
        
        
        # blitting score and level
        score = font_small.render(str(SCORE), True, RED)
        level = font_small.render(str(LEVEL), True, YELLOW)
        screen.blit(score , (10,10))
        screen.blit(level , (780,10))
        #drawing body ,head and food
        S.draw_head()
        S.draw_body()
        F.draw()
        # condition for poison
        if cnt % 3 == 0 and cnt != 0:
            P.draw()
        # condition for level
        if LEVEL == 2:
            L.level1()
        
        draw_grid()
        
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()