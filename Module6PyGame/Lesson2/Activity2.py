import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False

PALE_TURQUOISE = (175, 238, 238)
DARK_MAGENTA = (139, 0, 139)

screen.fill(PALE_TURQUOISE)

pygame.draw.circle(screen, DARK_MAGENTA, (100,100),50, 2)

pygame.draw.circle(screen, DARK_MAGENTA, (250,250),50)

pygame.display.update()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =  True
    
    pygame .display.flip()

pygame.quit()