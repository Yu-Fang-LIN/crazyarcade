from tkinter import CENTER
from turtle import right, up
import pygame
import random
from pygame.locals import *

from main import explosion

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super(Player, self).__init__()              
        self.surf = pygame.Surface((34, 34))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = (x, y))
        self.dirct = (0, 0) #walking direction
        self.collision = False
        self.bomb_num = 1
        self.bomb_num_max = 5
        self.bomb_rate = 3000
        self.bomb_explosion_rate = 3000
        self.bomb_power = 1

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
        if pressed_keys[K_LSHIFT] and self.at_center():
            if self.bomb_num > 0:
                bomb = Bomb(self.rect.x + 17, self.rect.y + 17, self, self.bomb_power)
                all_sprites.add(bomb)
                bombs.add(bomb)
                self.bomb_num -= 1


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
        if pressed_keys[K_RSHIFT] and self.at_center():
            if self.bomb_num > 0:
                bomb = Bomb(self.rect.x + 17, self.rect.y + 17, self, self.bomb_power)
                all_sprites.add(bomb)
                bombs.add(bomb)
                self.bomb_num -= 1


#create wood for building a map
class Wood(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 38, height = 38):
        super(Wood, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((204, 119, 35))
        self.rect = self.surf.get_rect(
            center=(x, y, ))

#create rock for building a map
class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 38, height = 38):
        super(Rock, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((89, 90, 92))
        self.rect = self.surf.get_rect(
            center=(x, y, ))

class Explosion(pygame.sprite.Sprite):#爆炸範圍
    def __init__(self, x, y, direct, power): #size:tuple
        super(Explosion, self).__init__()
        self.direct = direct
        self.surf = pygame.Surface((30, 30))
        # self.surf.fill((222, 169, 151))#淡紅色
        self.rect = self.surf.get_rect(center = (x, y, ))
        self.range = 0 #爆炸範圍現在到哪
        self.power = power #爆炸威力
    def update1(self):
        if self.direct == 'right' and self.range < self.power:
            self.rect.move_ip(40, 0)
            self.surf.fill((222, 169, 151))#淡紅色
            self.range += 1
        elif self.direct =='down' and self.range < self.power:
            self.rect.move_ip(0, 40)
            self.surf.fill((222, 169, 151))
            self.range += 1
        elif self.direct =='up' and self.range < self.power:
            self.rect.move_ip(0, -40)
            self.surf.fill((222, 169, 151))
            self.range += 1
        elif self.direct =='left' and self.range < self.power:
            self.rect.move_ip(-40, 0)
            self.surf.fill((222, 169, 151))
            self.range += 1
        elif self.range == self.power: #不能馬上爆,因為要計算碰撞,所以下一個迴圈再爆
            self.range += 1 
        elif self.range > self.power:
            self.kill()
        if pygame.sprite.spritecollideany(self, rocks):
            self.kill()

                       
        
class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, owner, power):
        super(Bomb, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((245, 43, 2))
        self.rect = self.surf.get_rect(center = (x, y, ))
        self.owner = owner
        self.start = pygame.time.get_ticks() #計時炸彈
        self.timer = pygame.time.get_ticks()
class MorePower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MorePower, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((154, 74, 224))
        self.rect = self.surf.get_rect(center = (x, y, ))
   

# Initialize pygame
pygame.init()

# create players
player1, player2 = Player(261, 166, (13, 217, 84)), Player(741, 486, (31, 46, 181))

# player1 gets bombs 
ADDBOMB1 = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBOMB1, player1.bomb_rate) # get a bomb per [player1.bomb_rate] seconds
# player2 gets bombs 
ADDBOMB2 = pygame.USEREVENT + 2
pygame.time.set_timer(ADDBOMB2, player2.bomb_rate) # get a bomb per [player2.bomb_rate] seconds

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create groups
woods = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bombs = pygame.sprite.Group()
players = pygame.sprite.Group()
destructible = pygame.sprite.Group()
explosions = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_wall = pygame.sprite.Group()
morepowers = pygame.sprite.Group()

all_sprites.add(player1, player2)
players.add(player1, player2)
destructible.add(player1, player2)

def explo(bomb, power):
    explosion1 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'up', power)
    explosion2 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'down', power)
    explosion3 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'left', power)
    explosion4 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'right', power)
    all_sprites.add(explosion1, explosion2, explosion3, explosion4)
    explosions.add(explosion1, explosion2, explosion3, explosion4)

# Build map
# block_center = (141+40k, 46+40k) block_size = (38,38)
with open("map1.txt", "r") as f:
    h = 46
    for line in f.readlines():
        w = 141
        for s in line:
            if s == "0":
                pass
            elif s == "1":
                wood = Wood(w, h)
                woods.add(wood)
                all_sprites.add(wood)
                all_wall.add(wood)
                destructible.add(wood)
                fall = random.random()                
            elif s == "2":
                rock = Rock(w, h)
                Rock.add(rock)
                all_sprites.add(rock)
                all_wall.add(rock)
            w += 40
        h += 40

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
        
        # add a bomb
        if event.type == ADDBOMB1:
            if player1.bomb_num < player1.bomb_num_max:
                player1.bomb_num += 1
        if event.type == ADDBOMB2:
            if player2.bomb_num < player2.bomb_num_max:
                player2.bomb_num += 1
    
    # Get the set of keys pressed and check for user input
    # if players are not at center, they keep moving until arriving at the center
    pressed_keys = pygame.key.get_pressed()
    if player1.at_center() or player1.dirct == (0, 0): 
        player1.update1(pressed_keys)
    else:
        player1.rect.move_ip(player1.dirct[0], player1.dirct[1])
        if pygame.sprite.spritecollideany(player1, all_wall): #if the player met the wall, come back to previous position and stop keeping moving
            player1.rect.move_ip(-player1.dirct[0], -player1.dirct[1])
            player1.collision = True
            player1.dirct = (0, 0)

    if player2.at_center() or player2.dirct == (0, 0):
        player2.update2(pressed_keys)
    else:
        player2.rect.move_ip(player2.dirct[0], player2.dirct[1])
        if pygame.sprite.spritecollideany(player2, all_wall): #if the player met the wall, come back to previous position and stop keeping moving
            player2.rect.move_ip(-player2.dirct[0], -player2.dirct[1])
            player2.collision = True
            player2.dirct = (0, 0)
    a = pygame.sprite.groupcollide(explosions, destructible, True, True)
    if a != {}:
        for obj in a:
            if random.random() > 0.7:
                morepower = MorePower(obj.rect.center[0], obj.rect.center[1])
                morepowers.add(morepower)
                all_sprites.add(morepower)
    
    # bomb explosion
    for bomb in bombs:
        bomb.timer += 1000 / 30
        if bomb.timer - bomb.start >= player1.bomb_explosion_rate and bomb.owner == player1:
            explo(bomb, player1.bomb_power)
            bomb.kill()
        if bomb.timer - bomb.start >= player2.bomb_explosion_rate and bomb.owner == player2:
            explo(bomb, player2.bomb_power)
            bomb.kill()

    # check if players are alive
    if player1 not in all_sprites:
        player1.kill()
        running = False
        print("player2 is winner!")
    elif player2 not in all_sprites:
        player2.kill()
        running = False
        print("player1 is winner!")

    # Fill the screen with black
    screen.fill((0, 0, 0))

    b = pygame.sprite.groupcollide(players, morepowers, False, True)# 撿威力藥水
    if b != {}:
        for player in players:
            player.bomb_power += 1
    
    if len(explosions) != 0:
        print(len(explosions))

    # update炸彈範圍
    for obj in explosions:
        obj.update1()

    # Draw things on the screen
    for obj in all_sprites:
        screen.blit(obj.surf, obj.rect)

    # Update the display
    pygame.display.update()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)