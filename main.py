import pygame#23
import random
from pygame.locals import *

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super(Player, self).__init__()              
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = (x, y))
        self.dirct = (0, 0) #walking direction

    # whether the player is at block_center or not
    def at_center(self):
        return ((self.rect.center[0] - 141) % 40 == 0) and ((self.rect.center[1] - 46) % 40 == 0)

    # Move the sprite based on user keypresses #player1
    def update1(self, pressed_keys):          
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
            self.dirct = (0, -5)
            if pygame.sprite.spritecollideany(player1, all_wall):
                self.rect.move_ip(0, 5)
                self.dirct = (0, 0)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
            self.dirct = (0, 5)
            if pygame.sprite.spritecollideany(player1, all_wall):
                self.rect.move_ip(0, -5)
                self.dirct = (0, 0)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
            self.dirct = (-5, 0)
            if pygame.sprite.spritecollideany(player1, all_wall):
                self.rect.move_ip(5, 0)
                self.dirct = (0, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
            self.dirct = (5, 0)
            if pygame.sprite.spritecollideany(player1, all_wall):
                self.rect.move_ip(-5, 0)
                self.dirct = (0, 0)
        if pressed_keys[K_LSHIFT]:
            bomb = Bomb(self.rect.x + 18, self.rect.y + 18)
            all_sprites.add(bomb)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update2(self, pressed_keys): #player2
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.dirct = (0, -5)
            if pygame.sprite.spritecollideany(player2, all_wall):
                self.rect.move_ip(0, 5)
                self.dirct = (0, 0)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.dirct = (0, 5)
            if pygame.sprite.spritecollideany(player2, all_wall):
                self.rect.move_ip(0, -5)
                self.dirct = (0, 0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.dirct = (-5, 0)
            if pygame.sprite.spritecollideany(player2, all_wall):
                self.rect.move_ip(5, 0)
                self.dirct = (0, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.dirct = (5, 0)
            if pygame.sprite.spritecollideany(player2, all_wall):
                self.rect.move_ip(-5, 0)
                self.dirct = (0, 0)
        if pressed_keys[K_RSHIFT]:
            bomb = Bomb(self.rect.x + 18, self.rect.y + 18)
            all_sprites.add(bomb)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#create wood for building a map
class Wood(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 38, height = 38):
        super(Wood, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((204, 119, 35))
        self.rect = self.surf.get_rect(
            center=(x, y, ))
        self.speed = 0

#create rock for building a map
class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 38, height = 38):
        super(Rock, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((89, 90, 92))
        self.rect = self.surf.get_rect(
            center=(x, y, ))
        self.speed = 0

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bomb, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((245, 43, 2))
        self.rect = self.surf.get_rect(center = (x, y, ))
        self.speed = 0

# Initialize pygame
pygame.init()

player1, player2 = Player(261, 166, (13, 217, 84)), Player(741, 486, (31, 46, 181))

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
woods = pygame.sprite.Group()
rocks = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_wall = pygame.sprite.Group()
all_sprites.add(player1, player2)

# Build map
# block_center = (141+40k, 46+40k) block_size = (38,38)
for i in range(181, 822, 40):
    wood = Wood(i, 86)
    woods.add(wood)
    all_sprites.add(wood)
    all_wall.add(wood)
    wood = Wood(i, 566)
    woods.add(wood)
    all_sprites.add(wood)
    all_wall.add(wood)
for i in range(86, 567, 40):
    wood = Wood(181, i)
    woods.add(wood)
    all_sprites.add(wood)
    all_wall.add(wood)
    wood = Wood(821, i)
    woods.add(wood)
    all_sprites.add(wood)
    all_wall.add(wood)
for i in range(141, 862, 40):
    rock = Rock(i, 46)
    Rock.add(rock)
    all_sprites.add(rock)
    all_wall.add(rock)
    rock = Rock(i, 606)
    Rock.add(rock)
    all_sprites.add(rock)
    all_wall.add(rock)
for i in range(86, 567, 40):
    rock = Rock(141, i)
    Rock.add(rock)
    all_sprites.add(rock)
    all_wall.add(rock)
    rock = Rock(861, i)
    Rock.add(rock)
    all_sprites.add(rock)
    all_wall.add(rock)
# small_points_center = (201+40k, 106+40k), size = (2, 2)
for i in range(201, 802, 40):
    for j in range(106, 547, 40):
        rock = Rock(i, j, 2, 2)
        Rock.add(rock)
        all_sprites.add(rock)
        all_wall.add(rock)        

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False 
    
    # Get the set of keys pressed and check for user input
    # if players are not at center, they keep moving until arriving at the center
    pressed_keys = pygame.key.get_pressed()
    if player1.at_center():
        player1.update1(pressed_keys)
    else:
        player1.rect.move_ip(player1.dirct[0], player1.dirct[1])

    if player2.at_center():
        player2.update2(pressed_keys)
    else:
        player2.rect.move_ip(player2.dirct[0], player2.dirct[1])
        
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)

    for obj in all_sprites:
        screen.blit(obj.surf, obj.rect)
    
    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
