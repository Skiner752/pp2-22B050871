import pygame

pygame.init()
width = 510
height = 510
screen = pygame.display.set_mode((width, height))
done = False
ball_x = 25
ball_y = 25
colour_red = (255, 0, 0)
clock = pygame.time.Clock()
pygame.display.set_caption("Red Ball")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and ball_y > 25:
        ball_y -= 20
    if pressed[pygame.K_DOWN] and ball_y < height - 25:
        ball_y += 20
    if pressed[pygame.K_LEFT] and ball_x > 25:
        ball_x -= 20
    if pressed[pygame.K_RIGHT] and ball_x < width - 25:
        ball_x += 20

    screen.fill((255, 255, 250))
    pygame.draw.circle(screen, colour_red, (ball_x , ball_y), 25)
    pygame.display.flip()
    clock.tick(90)

# pygame.quit()

        

