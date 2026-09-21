import pygame
import random
 
pygame.init()
CAR_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
SIGNAL_CHANGE_EVENT = pygame.USEREVENT + 2
 
ROAD = pygame.Color("darkgray")
WHITE = pygame.Color("white")
YELLOW = pygame.Color("yellow")
BLUE = pygame.Color("blue")
ORANGE = pygame.Color("orange") 
RED = pygame.Color("red")
GREEN = pygame.Color("green")
 
class Car(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [3, 0]
 

    def update(self):
        self.rect.move_ip(self.velocity)
 
        sensor_triggered = False
        if self.rect.left <= 0 or self.rect.right >= 600:
            self.velocity[0] = -self.velocity[0]
 
            sensor_triggered = True
        if sensor_triggered:
            pygame.event.post(pygame.event.Event(CAR_COLOR_CHANGE_EVENT))
 
            pygame.event.post(pygame.event.Event(SIGNAL_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([WHITE, YELLOW, BLUE, ORANGE]))
 
def change_signal():
    global signal_color

    if signal_color == RED:
        signal_color = GREEN
    else:
        signal_color = RED
 
all_sprites = pygame.sprite.Group() 
car = Car(WHITE, 70, 35)

car.rect.x = 50
car.rect.y = 300
 
all_sprites.add(car)
 
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Smart Traffic Signal Simulator")
 
# Set the starting signal colour
signal_color = RED
 
# Create a clock to control the frame rate
clock = pygame.time.Clock()
 
# Control the game loop
running = True
 
while running:
 
    # Handle events
    for event in pygame.event.get():
 
        # Close the application
        if event.type == pygame.QUIT:
            running = False
 
        # Handle the custom car colour event
        elif event.type == CAR_COLOR_CHANGE_EVENT:
            car.change_color()
 
        # Handle the custom traffic signal event
        elif event.type == SIGNAL_CHANGE_EVENT:
            change_signal()
 
    # Update all sprites in the group
    all_sprites.update()
 
    # Draw the road background
    screen.fill(ROAD)
 
    # Draw road divider lines
    for x in range(0, 600, 80):
        pygame.draw.rect(
            screen,
            WHITE,
            (x, 345, 45, 5)
        )
 
    # Draw the traffic-signal box
    pygame.draw.rect(
        screen,
        pygame.Color("black"),
        (275, 40, 50, 90)
    )
 
    # Draw the active traffic-signal light
    pygame.draw.circle(
        screen,
        signal_color,
        (300, 85),
        20
    )
 
    # Draw all sprites
    all_sprites.draw(screen)
 
    # Refresh the display
    pygame.display.flip()
 
    # Limit the frame rate
    clock.tick(60)
 
# Close Pygame
pygame.quit()
