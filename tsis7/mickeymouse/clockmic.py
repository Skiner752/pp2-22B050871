import pygame
import datetime

pygame.init()
size_screen = (1000,1000)
done = False
WHITE = (255,255,255)
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode(size_screen)
center = screen.get_rect().center


clock_img = pygame.image.load('clock.png')
body_img = pygame.image.load('miki.png')
second_hand = pygame.image.load('arm2.png')
minute_hand = pygame.image.load('arm1.png')


clock_img = pygame.transform.scale(clock_img , (900 ,900))
body_img = pygame.transform.scale(body_img , (580 ,620))
second_hand =  pygame.transform.scale(second_hand , (370 ,100))
minute_hand =  pygame.transform.scale(minute_hand , (320,100))

def rotation(screen , image , pos , originPos ,angle):
    image_rect = image.get_rect(topleft = (pos[0]- originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    
    screen.blit(rotated_image, rotated_image_rect)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    current_date_time = datetime.datetime.now()
    minute = current_date_time.minute
    second = current_date_time.second
    
    
    screen.fill(WHITE)
    screen.blit(clock_img , (53,40))
    screen.blit(body_img , (210,140))
    
    
    # Minute
    theta = (minute + second / 60 ) * (360/60)
    rotation(screen , minute_hand , center , (minute_hand.get_width() / 2 + 120 , minute_hand.get_height() / 2 + 30) , theta + 75)
    
    #Second
    theta = second * (360/60)
    rotation(screen , second_hand , center , (second_hand.get_width() / 2 - 150 , second_hand.get_height() / 2 ) , theta - 87 ) # theta - value = промах ее
    
    
    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()