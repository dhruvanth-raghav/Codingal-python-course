import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

PALE_TURQUOISE = (175, 238, 238)
DARK_MAGENTA = (139, 0, 139)
LIME_GREEN = (50, 205, 50)
RED = (255, 0, 0)
WHITE = (255,255,255)


current_colour = WHITE


X,Y = 30,30
sprite_width, sprite_height = 60,60

clock =pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =  True

    pressed = pygame.key.get_pressed()        

    if pressed[pygame.K_LEFT]:
        X -= 3

    if pressed[pygame.K_RIGHT]:
        X += 3

    if pressed[pygame.K_UP]:
        Y -= 3

    if pressed[pygame.K_DOWN]:
        Y += 3


    X = min(max(0, X),SCREEN_WIDTH - sprite_width)
    Y = min(max(0,Y),SCREEN_HEIGHT - sprite_height)

    if X ==0:
        current_colour = DARK_MAGENTA
    elif X== SCREEN_WIDTH - sprite_width:
        current_colour = PALE_TURQUOISE
    elif Y ==0:
        current_colour = LIME_GREEN

    elif Y == SCREEN_HEIGHT - sprite_height:
        current_colour = RED

    screen.fill((0,0,0))
    pygame.draw.rect(screen, current_colour, (X, Y, sprite_width, sprite_height))


    pygame .display.flip()
    clock.tick(90)

pygame.quit()