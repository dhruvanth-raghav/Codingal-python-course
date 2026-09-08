import pygame

pygame.init()

#Setup the window geometry
screen = pygame.display.set_mode((600,600))

#Create a loop to run the game until finish
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
