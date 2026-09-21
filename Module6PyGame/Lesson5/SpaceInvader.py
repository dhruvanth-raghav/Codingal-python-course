import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEM_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEM_HEIGHT))

IMAGE_BASE_PATH = "Module6PyGame\\Lesson5\\"


background = pygame.image.load(IMAGE_BASE_PATH+'background.png')

pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load(IMAGE_BASE_PATH+'ufo.png')
pygame.display.set_icon(icon)

playerImage = pygame.image.load(IMAGE_BASE_PATH+'player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImage.append(pygame.image.load(IMAGE_BASE_PATH+'enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImage = pygame.image.load(IMAGE_BASE_PATH+'bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.SysFont('Times New Roman',32)
textX = 10
textY = 10

over_font = pygame.font.SysFont('Times New Roman',64)

def show_score(x, y):
    score = font.render("Score:"+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def gameOver_txt():
    over_txt = over_font.render("GAME OVER", True,(255, 255, 255))
    screen.blit(over_txt, (200, 250))

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImage[i],(x, y))

def fireBullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, ( x +16, y + 10))

def isCollision(enemyX, enemyY, bulletX , bulletY):
    distance = math.sqrt((enemyX - bulletX) **2 + (enemyY - bulletY) **2)
    return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0 ,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fireBullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT ]:
            playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX,SCREEN_WIDTH - 64))

    for i in range(num_of_enemies):
        if enemyY[i] >  340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            gameOver_txt()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if isCollision(enemyX[i],enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value +=1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

