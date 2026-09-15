import pygame
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

font = pygame.font.SysFont("Times New Roman",FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image, colour, pygame.Rect(0,0, width , height))
        self.rect = self.image.get_rect()


    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SPRITE COLLISION")
all_sprites = pygame.sprite.Group()

#create the sprites
sprite1= Sprite((199, 21, 133), 20, 30)
sprite1.rect.x =  random.randint(0 , SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0 , SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2= Sprite((106, 90, 205), 20, 30)
sprite2.rect.x =  random.randint(0 , SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0 , SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

running = True
won =  False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED            
        print(x_change, y_change)
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    if won:
        winTxt = font.render("YOU WIN!", True, pygame.Color("white"))
        screen.blit(winTxt, (
            (SCREEN_WIDTH - winTxt.get_width()) // 2,
            (SCREEN_WIDTH - winTxt.get_width()) // 2

        ))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()