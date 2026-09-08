import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600

#Setup the window geometry
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Adding image and background image")

backGround_image=pygame.transform.scale(
    pygame.image.load(r"Module6PyGame\Lesson1\background.jpg").convert(),
    (SCREEN_WIDTH,SCREEN_HEIGHT)
)

penguin_image = pygame.transform.scale(
    pygame.image.load(r"Module6PyGame\Lesson1\pygame-penguin.png").convert_alpha(),
    (200,200)
)

penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2-30))

text = pygame.font.Font(None, 36).render("Hello, Penguin!",True, pygame.Color("white"))

text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+110))


def game_loop():
    clock = pygame.time.Clock()

    #Create a loop to run the game until finish
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        display_surface.blit(backGround_image, (0,0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text,text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()  


if __name__ == "__main__":
    game_loop()