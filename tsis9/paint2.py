import pygame
import random
import math

# Making screen
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('PAINT')
# boolean variables for the game
done = False
draw_on = False
erase_on = False
check = False
draw_rect = False
draw_sq = False
draw_circ = False
draw_e_tr = False
draw_rb = False
draw_r_tr = False
# started position of the figures
last_pos = (0, 0)
e_last_pos = (1,1)
r_last_pos = (0,0)
s_last_pos = (0,0)
e_tr_last_pos = (0,0)
rb_last_pos = (0,0)
r_tr_last_pos = (0,0)
# colours selection
colour = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
PURPLE = (240,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)

# Radius of the Brush
radius = 5
e_radius = 10
rect_radius = 5
c_radius = 10
s_radius = 5
e_tr_radius = 5
rb_radius = 6
r_tr_radius = 5
screen.fill((255,255,255))

def draw_right(screen,colour , start , end , width): # function for drawing right triangle
    x , y = start[0] , start[1]
    x1 , y1 = end[0] , end[1]
    x2 , y2 = x , y1
    points = [(x,y) , (x1,y1) , (x2,y2)]
    pygame.draw.polygon(screen , colour , points , width)

def draw_rhombus(screen , colour , start , end , width): # function for drawing rhombus
    x , y = start[0] , start[1]
    x1 , y1 = end[0] , end[1]
    d = ((x1-x)**2 + (y1-y)**2) ** 0.5
    xc , yc  = (x + x1)/2 , (y+y1) / 2
    xr , yr = xc + d , yc
    xl , yl = xc -d , yc
    points = [(x,y) , (xl,yl) , (x1,y1) , (xr , yr)]
    pygame.draw.polygon(screen , colour , points , width)

def draw_e_triangle(screen , colour , start , end , width): # function for drawing equaliteral triangle
    x , y = start[0] , start[1]
    x1 , y1 = end[0] , end[1]
    a = ((x1-x)**2 + (y1-y)**2) ** 0.5
    xc , yc = (x + x1)/2 , (y+y1) / 2
    xv , yv = xc , yc - a
    points = [(x ,y) , (x1,y1) , (xv , yv)]
    pygame.draw.polygon(screen , colour  , points , width)

def draw_circle(screen, colour, pos, radius, initial):# function for drawing circle 
    x1, y1 = initial
    x2, y2 = pos
    
    radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    pygame.draw.circle(screen, colour, pos, radius, 10)

def draw_square(screen , colour , start , end , width): # function for drawing square
    # a = d/sqrt(2)
    c = 2**0.5
    x , y = start[0] , start[1]
    x1 , y1 = end[0] , end[1]
    d = ((x1-x)**2 + (y1-y)**2)**0.5
    a = d/c
    pygame.draw.rect(screen , colour , (x,min(y,y1),a,a) , width)

def draw_rectangle(screen ,start , end , width , colour ):  # function for drawing rectangle   
   x1 , x2 = start[0] , end[0]
   y1 , y2 = start[1] , end[1]
   height = abs(y1 - y2)
   widthr = abs(x1 - x2)
   pygame.draw.rect(screen, colour, (x1, min(y1, y2), widthr, height), width)

def roundline(screen, colour, start, end, radius=1) : # function for drawing lines
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(screen, colour, (x, y), radius)


while not done : # main game loop
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
            pygame.quit()

        if event.type == pygame.KEYDOWN: # if some keyboard is pressed
            if event.key == pygame.K_r:
                colour = RED
                check = False
                draw_rect = False
                draw_circ = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            if event.key == pygame.K_p:
                colour = PURPLE
                check = False
                draw_rect = False
                draw_circ = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            if event.key == pygame.K_b:
                colour = BLUE
                check = False
                draw_rect = False
                draw_circ = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            if event.key == pygame.K_l:
                colour = BLACK
                check = False
                draw_rect = False
                draw_circ = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            if event.key == pygame.K_g:
                colour = GREEN
                check = False
                draw_rect = False
                draw_circ = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            if event.key == pygame.K_1: # left click grows radius
                radius = min(200, radius + 1)
            elif event.key == pygame.K_2: # right click shrinks radius
                radius = max(1, radius - 1)
            #Eraser
            if event.key == pygame.K_9:
                e_radius = min(200, e_radius + 1)
            elif event.key == pygame.K_0:
                e_radius = max(1 , e_radius-1)
        
            if event.key == pygame.K_e:
                check = True
                draw_rect = False
                draw_circ = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            # rectangle
            if event.key == pygame.K_c:
                draw_rect = True
                draw_circ = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            #circle
            if event.key == pygame.K_u:
                draw_circ = True
                draw_rect = False
                draw_sq = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            # square
            if event.key == pygame.K_s:
                draw_sq = True
                draw_circ = False
                draw_rect = False
                draw_e_tr = False
                draw_rb = False
                draw_r_tr = False
            # equilateral triangle
            if event.key == pygame.K_q:
                draw_e_tr = True
                draw_circ = False
                draw_rect = False
                draw_sq = False
                draw_rb = False
                draw_r_tr = False
            #rhombus
            if event.key == pygame.K_b:
                draw_rb = True
                draw_e_tr = False
                draw_circ = False
                draw_rect = False
                draw_sq = False
                draw_r_tr = False
            if event.key == pygame.K_h:
                draw_r_tr = True
                draw_rb = False
                draw_e_tr = False
                draw_circ = False
                draw_rect = False
                draw_sq = False
                
        # right triangle
        if event.type == pygame.MOUSEBUTTONDOWN and draw_r_tr:
            r_tr_last_pos = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP and draw_r_tr:
            draw_right(screen , colour , r_tr_last_pos , event.pos , r_tr_radius) 
        
        # rhombus
        if event.type == pygame.MOUSEBUTTONDOWN and draw_rb:
            rb_last_pos = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP and draw_rb:
            draw_rhombus(screen , colour , rb_last_pos , event.pos , rb_radius)
        # equilateral triangle
        if event.type == pygame.MOUSEBUTTONDOWN and draw_e_tr:
            e_tr_last_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP and draw_e_tr:
            draw_e_triangle(screen , colour , e_tr_last_pos , event.pos , e_tr_radius)

        #Square
        if event.type == pygame.MOUSEBUTTONDOWN and draw_sq:
            s_last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP and draw_sq:
            draw_square(screen , colour , s_last_pos , event.pos , s_radius)

        # Rectangle
        if event.type == pygame.MOUSEBUTTONDOWN and draw_rect:
            r_last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP and draw_rect:
            draw_rectangle(screen , r_last_pos , event.pos , rect_radius , colour)
            
        
        #Circle
        if event.type == pygame.MOUSEBUTTONDOWN and draw_circ:
            point = event.pos

        if event.type == pygame.MOUSEBUTTONUP and draw_circ:
            draw_circle(screen , colour , event.pos , c_radius , point)


        # Eraser            
        if event.type == pygame.MOUSEBUTTONDOWN and check and draw_rect == False and draw_circ == False and draw_sq == False and draw_e_tr == False and draw_rb == False and draw_r_tr == False:
            pygame.draw.circle(screen, WHITE, event.pos, e_radius)
            erase_on = True
        if event.type == pygame.MOUSEBUTTONUP and check and draw_rect == False and draw_circ == False and draw_sq == False and draw_e_tr == False and draw_rb == False and draw_r_tr == False: 
            erase_on = False 
        if event.type == pygame.MOUSEMOTION and check and draw_rect == False and draw_circ == False and draw_sq == False and draw_e_tr == False and draw_rb == False and draw_r_tr == False:
            if erase_on:
                pygame.draw.circle(screen, WHITE, event.pos, e_radius)
            e_last_pos = event.pos  
        
        # Draw 
        if event.type == pygame.MOUSEBUTTONDOWN and check == False and draw_rect == False and draw_circ == False and draw_sq == False and draw_e_tr == False and draw_rb == False and draw_r_tr == False:
                pygame.draw.circle(screen, colour, event.pos, radius)
                draw_on = True
        if event.type == pygame.MOUSEBUTTONUP and check == False and draw_rect == False and draw_circ == False and draw_sq == False and draw_e_tr == False and draw_rb == False and draw_r_tr == False:
            draw_on = False
        if event.type == pygame.MOUSEMOTION  and check == False and draw_rect == False and draw_sq == False and draw_circ == False and draw_e_tr == False and draw_rb == False and draw_r_tr == False:
            if draw_on :
                pygame.draw.circle(screen, colour, event.pos, radius)
                roundline(screen, colour, event.pos, last_pos, radius)
            last_pos = event.pos
            
    pygame.display.flip()



