from turtle import circle
import pygame
import random
from pygame.locals import *
from Shrinkcircle import *

# Define constants for the screen width and height
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 650

# 圖片庫
cmkuan = {'right':['角色一館爺\館爺右轉 reset.png', '角色一館爺\館爺右轉1.png', '角色一館爺\館爺右轉2.png'],
    'left':['角色一館爺\館爺左轉 reset.png', '角色一館爺\館爺左轉1.png', '角色一館爺\館爺左轉2.png'],
    'up':['角色一館爺\館爺往上 reset.png', '角色一館爺\館爺往上1.png', '角色一館爺\館爺往上2.png'],
    'down':['角色一館爺\館爺往下 reset ( 初始).png', '角色一館爺\館爺往下1.png', '角色一館爺\館爺往下2.png'],
    'still':['角色一館爺\館爺右轉 reset.png', '角色一館爺\館爺右轉 reset.png', '角色一館爺\館爺右轉 reset.png']}
kp = {'right':['角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p右轉 reset.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p右轉 1.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p右轉 2.png'],
    'left':['角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p左轉 reset.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p左轉 1.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p左轉 2.png'],
    'up':['角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p往上 reset.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p往上 1.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p往上 2.png'],
    'down':['角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p往下 reset (初始).png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p往下 1.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p往下 2.png'],
    'still':['角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p右轉 1.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p右轉 1.png', '角色二 柯p-20220116T111211Z-001\角色二 柯p\柯p右轉 1.png']}
props = ['道具包\地雷.png', '道具包\威力藥水.png', '道具包\炸彈.png', '道具包\槍槍.png', '道具包\加速藥水.png']   

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, name):
        super(Player, self).__init__()
        self.name = name              
        self.surf = pygame.Surface((34, 34))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = (x, y))
        self.dirct = (0, 0) #walking direction
        self.direction = 'still'
        self.collision = False
        self.bomb_num = 1
        self.bomb_num_max = 5
        self.bomb_rate = 3000 #炸彈填充時間
        self.get_bomb_start = 0
        self.get_bomb_timer = 0
        self.bomb_explosion_rate = 3000 #炸彈爆炸時間
        self.bomb_power = 1
        self.walk_rate = 5
        self.energy = 0 #能量
        # 加這兩行是為了修重複讀取shift鍵導致一次放置多個炸彈的bug 2022/1/14 04:40 a.m.
        self.bomb_set_time = 7
        self.start = 8
        self.animation = 0
        self.shoot = False #是否正在開槍

    # whether the player is at block_center or not
    def at_center(self):
        return ((self.rect.center[0] - 291) % 40 == 0) and ((self.rect.center[1] - 46) % 40 == 0)

    # Move the sprite based on user keypresses #player1
    def update1(self, pressed_keys):
        if self.at_center() or self.dirct == (0, 0):           
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -self.walk_rate)
                self.dirct = (0, -self.walk_rate)
                if pygame.sprite.spritecollideany(self, all_wall):
                    self.rect.move_ip(0, self.walk_rate)
                    self.dirct = (0, 0)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, self.walk_rate)
                self.dirct = (0, self.walk_rate)
                if pygame.sprite.spritecollideany(self, all_wall):
                    self.rect.move_ip(0, -self.walk_rate)
                    self.dirct = (0, 0)
            if pressed_keys[K_a]:
                self.rect.move_ip(-self.walk_rate, 0)
                self.dirct = (-self.walk_rate, 0)
                if pygame.sprite.spritecollideany(self, all_wall):
                    self.rect.move_ip(self.walk_rate, 0)
                    self.dirct = (0, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(self.walk_rate, 0)
                self.dirct = (self.walk_rate, 0)
                if pygame.sprite.spritecollideany(self, all_wall):
                    self.rect.move_ip(-self.walk_rate, 0)
                    self.dirct = (0, 0)
            if pressed_keys[K_LSHIFT] and self.at_center() and self.start > self.bomb_set_time:
                if self.bomb_num > 0:
                    bomb = Bomb(self.rect.center[0], self.rect.center[1], self, self.bomb_power)
                    all_sprites.add(bomb)
                    bombs.add(bomb)
                    self.bomb_num -= 1
                    self.start = 0
            if self.start <= self.bomb_set_time:# 限制炸彈設置的間隔,以防重複讀取shift鍵
                self.start += 1
        else:
            self.rect.move_ip(self.dirct[0], self.dirct[1])
            if pygame.sprite.spritecollideany(self, all_wall): #if the player met the wall, come back to previous position and stop keeping moving
                self.rect.move_ip(-self.dirct[0], -self.dirct[1])
                self.collision = True
                self.dirct = (0, 0)
        # 槍
        if pressed_keys[K_z] and self.energy > 0:
            bullet = Bullet(self.rect.center[0], self.rect.center[1], self)
            all_sprites.add(bullet)
            bullets.add(bullet)
            self.energy -= 1
            self.shoot = True
        else:
            self.shoot = False
        # 地雷
        if pressed_keys[K_x] and self.energy == 5:
            mine = Mine(self.rect.center[0], self.rect.center[1], self)
            all_sprites.add(mine)
            mines.add(mine)
            self.energy = 0        

    def update2(self, pressed_keys): #player2
        if player2.at_center() or player2.dirct == (0, 0):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -self.walk_rate)
                self.dirct = (0, -self.walk_rate)
                if pygame.sprite.spritecollideany(player2, all_wall):
                    self.rect.move_ip(0, self.walk_rate)
                    self.dirct = (0, 0)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.walk_rate)
                self.dirct = (0, self.walk_rate)
                if pygame.sprite.spritecollideany(player2, all_wall):
                    self.rect.move_ip(0, -self.walk_rate)
                    self.dirct = (0, 0)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-self.walk_rate, 0)
                self.dirct = (-self.walk_rate, 0)
                if pygame.sprite.spritecollideany(player2, all_wall):
                    self.rect.move_ip(self.walk_rate, 0)
                    self.dirct = (0, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.walk_rate, 0)
                self.dirct = (self.walk_rate, 0)
                if pygame.sprite.spritecollideany(player2, all_wall):
                    self.rect.move_ip(-self.walk_rate, 0)
                    self.dirct = (0, 0)
            if pressed_keys[K_RSHIFT] and self.at_center() and self.start > self.bomb_set_time:
                if self.bomb_num > 0:
                    bomb = Bomb(self.rect.center[0], self.rect.center[1], self, self.bomb_power)
                    all_sprites.add(bomb)
                    bombs.add(bomb)
                    self.bomb_num -= 1
                    self.start = 0
            if self.start <= self.bomb_set_time:
                self.start += 1
        else:
            player2.rect.move_ip(player2.dirct[0], player2.dirct[1])
            if pygame.sprite.spritecollideany(player2, all_wall): #if the player met the wall, come back to previous position and stop keeping moving
                player2.rect.move_ip(-player2.dirct[0], -player2.dirct[1])
                player2.collision = True
                player2.dirct = (0, 0)
        # 槍
        if pressed_keys[K_RCTRL] and self.energy > 0:
            bullet = Bullet(self.rect.center[0], self.rect.center[1], self)
            all_sprites.add(bullet)
            bullets.add(bullet)
            self.energy -= 1
            self.shoot = True
        else:
            self.shoot = False
            
        # 地雷
        if pressed_keys[K_RALT] and self.energy == 5:
            mine = Mine(self.rect.center[0], self.rect.center[1], self)
            all_sprites.add(mine)
            mines.add(mine)
            self.energy = 0

    # 畫能量條
    def draw(self, screen):
        pygame.draw.rect(screen, (115, 114, 114), (self.rect.x - 2, self.rect.y - 10, 39, 8), 2)
        pygame.draw.rect(screen, (2, 250, 242), (self.rect.x, self.rect.y - 8, 7 * self.energy, 4), 0)
    
    def anim(self, person):
        # 判斷direction
        if self.dirct == (0, 0):
            self.direction = 'still'
        elif self.dirct[0] > 0:
            self.direction = 'right'
        elif self.dirct[0] < 0:
            self.direction = 'left'
        elif self.dirct[1] > 0:
            self.direction = 'down'
        elif self.dirct[1] < 0:
            self.direction = 'up'
        # 走路的圖片
        if self.animation > 2:
            self.animation = 0
        head = pygame.image.load(person[self.direction][self.animation])
        head1 = pygame.transform.scale(head, (38, 38)) #改尺寸
        screen.blit(head1, (self.rect.x, self.rect.y))
        self.animation += 1 #換一張圖片
        # 開槍畫面
        if self.shoot:
            gun = pygame.image.load(props[3]).convert()
            if self.name == 'player1':
                gun2 = pygame.transform.rotozoom(gun, 270, 1)
            else:
                gun2 = pygame.transform.rotozoom(gun, 90, 1)
            screen.blit(gun2, (self.rect.x+30, self.rect.y))
            
#create wood for building a map
class Wood(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 38, height = 38):
        super(Wood, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((204, 119, 35))
        self.rect = self.surf.get_rect(
            center=(x, y, ))
    def anim(self):
        head = pygame.image.load('建築物\木頭.jpg')
        screen.blit(head, (self.rect.x, self.rect.y))

#create rock for building a map
class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 38, height = 38):
        super(Rock, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((89, 90, 92))
        self.rect = self.surf.get_rect(
            center=(x, y, ))
    def anim(self):
        head = pygame.image.load('建築物\石頭.png')
        screen.blit(head, (self.rect.x, self.rect.y))

class Explosion(pygame.sprite.Sprite):#爆炸衝擊波
    def __init__(self, x, y, direct, power, owner): #size:tuple
        super(Explosion, self).__init__()
        self.direct = direct
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((222, 169, 151))#淡紅色
        self.rect = self.surf.get_rect(center = (x, y, ))
        self.range = 0 #爆炸衝擊波現在到哪
        self.power = power #爆炸威力
        self.owner = owner #炸彈所有者
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
    def anim(self):
        head = pygame.image.load(props[2])
        screen.blit(head, (self.rect.x, self.rect.y))

class MorePower(pygame.sprite.Sprite):#威力藥水
    def __init__(self, x, y):
        super(MorePower, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((154, 74, 224))
        self.rect = self.surf.get_rect(center = (x, y, ))
    def anim(self):
        head = pygame.image.load(props[1])
        screen.blit(head, (self.rect.x, self.rect.y))

class Faster(pygame.sprite.Sprite):#威力藥水
    def __init__(self, x, y):
        super(Faster, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((250, 135, 187))
        self.rect = self.surf.get_rect(center = (x, y, ))
    def anim(self):
        head = pygame.image.load(props[4])
        screen.blit(head, (self.rect.x, self.rect.y))

class Bullet(pygame.sprite.Sprite):#子彈
    def __init__(self, x, y, owner):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((3, 3))
        self.surf.fill((200, 90, 20))
        self.rect = self.surf.get_rect(center = (x, y, ))
        self.owner = owner
    def position(self,x, y):
        self.rect = self.surf.get_rect(center = (x, y, ))

class Mine(pygame.sprite.Sprite):
    def __init__(self, x, y, owner):
        super(Mine, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((252, 211, 3))
        self.rect = self.surf.get_rect(center = (x, y, ))
        self.owner = owner
        self.start = pygame.time.get_ticks() #bomb_timer
        self.timer = pygame.time.get_ticks()
        self.invisible = False
    def anim(self):
        if not self.invisible:
            head = pygame.image.load(props[0])
            screen.blit(head, (self.rect.x, self.rect.y))
   


# Initialize pygame
pygame.init()

# create players
player1, player2 = Player(411, 166, (13, 217, 84), 'player1'), Player(891, 486, (31, 46, 181), 'player2')

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
fasters = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mines = pygame.sprite.Group()
roros = pygame.sprite.Group()

all_sprites.add(player1, player2)
players.add(player1, player2)
destructible.add(player1, player2)

# 生成四個方向的爆炸衝擊波
def explo(bomb, power, owner):
    explosion1 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'up', power, owner)
    explosion2 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'down', power, owner)
    explosion3 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'left', power, owner)
    explosion4 = Explosion(bomb.rect.center[0], bomb.rect.center[1], 'right', power, owner)
    all_sprites.add(explosion1, explosion2, explosion3, explosion4)
    explosions.add(explosion1, explosion2, explosion3, explosion4)

# Build map
# block_center = (291+40k, 46+40k) block_size = (38,38)
with open("map1.txt", "r") as f:
    h = 46
    for line in f.readlines():
        w = 291
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
                rocks.add(rock)
                all_sprites.add(rock)
                all_wall.add(rock)
                roros.add(rock)
            w += 40
        h += 40
# small_points_center = (201+40k, 106+40k), size = (2, 2)
for i in range(201+150, 802+150, 40):
    for j in range(106, 547, 40):
        rock = Rock(i, j, 2, 2)
        Rock.add(rock)
        all_sprites.add(rock)
        all_wall.add(rock)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

# 計時器
timer = 1

# 縮圈半徑
radius = 1300

# 縮圈圓心
circle_center = (random.randint(450, 850), random.randint(125, 325))

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
    player1.update1(pressed_keys)
    player2.update2(pressed_keys)

    # 背景 (星空會lag)
    # head = pygame.image.load('場景\籃球場.jpg')
    # screen.blit(head, (0, 0))

    # 去背
    player1.surf.set_alpha(0)
    player2.surf.set_alpha(0)
    for morepower in morepowers:
        morepower.surf.set_alpha(0)
    for bomb in bombs:
        bomb.surf.set_alpha(0)
    for faster in fasters:
        faster.surf.set_alpha(0)   

    # 填充炸彈
    if player1.bomb_num < player1.bomb_num_max:
        player1.get_bomb_timer += 30
    if player1.get_bomb_timer - player1.get_bomb_start >= player1.bomb_rate:
        player1.get_bomb_timer = 0
        player1.bomb_num += 1
    if player2.bomb_num < player2.bomb_num_max:
        player2.get_bomb_timer += 30
    if player2.get_bomb_timer - player2.get_bomb_start >= player2.bomb_rate:
        player2.get_bomb_timer = 0
        player2.bomb_num += 1

    # bomb explosion
    for bomb in bombs:
        bomb.timer += 1000 / 30
        if bomb.timer - bomb.start >= player1.bomb_explosion_rate and bomb.owner == player1:
            explo(bomb, player1.bomb_power, bomb.owner)
            bomb.kill()
        if bomb.timer - bomb.start >= player2.bomb_explosion_rate and bomb.owner == player2:
            explo(bomb, player2.bomb_power, bomb.owner)
            bomb.kill()

    # 判斷人有沒有被炸到 + 藥水掉落
    a = pygame.sprite.groupcollide(explosions, destructible, True, True)
    if a != {}:
        for obj in a:
            a = random.random()
            if obj.owner.energy < 5:
                obj.owner.energy += 1
            if a < 0.2:
                morepower = MorePower(obj.rect.center[0], obj.rect.center[1])
                morepowers.add(morepower)
                all_sprites.add(morepower)
            if a > 0.9:
                faster = Faster(obj.rect.center[0], obj.rect.center[1])
                fasters.add(faster)
                all_sprites.add(faster)

    # mine hide and wait for player pass
    for mine in mines:
        mine.timer += 1000 / 30
        if (mine.timer - mine.start) >= 1000: #地雷現形的時間
            mine.surf.fill((0, 0, 0))
            mine.invisible = True
            
        if mine.invisible:#有人踩到會死亡
            a = pygame.sprite.spritecollideany(mine, players) #a是踩到的人
            if a != None:
                a.kill()

    # 射子彈
    for bullet in bullets:
        if bullet.owner == player1:
            pos_x = bullet.rect.x + 1
            pos_y = bullet.rect.y + 1
            pos_y += 20
            bullet.position(pos_x, pos_y)
            if pygame.sprite.collide_rect(bullet, player2):
                player2.kill()
        if bullet.owner == player2:
            pos_x = bullet.rect.x + 1
            pos_y = bullet.rect.y + 1
            pos_y -= 20
            bullet.position(pos_x, pos_y)
            if pygame.sprite.collide_rect(bullet, player1):
                player1.kill()

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
    screen.fill((54, 54, 54))

    # 撿威力藥水
    b = pygame.sprite.groupcollide(players, morepowers, False, True)
    if b != {}:
        for player in b:
            player.bomb_power += 1

    # 撿加速藥水
    b = pygame.sprite.groupcollide(players, fasters, False, True)
    if b != {}:
        for player in b:
            player.bomb_rate *= 0.9
            if player.walk_rate == 5:
                player.walk_rate += 3
            elif player.walk_rate == 8: #跑速最多20
                player.walk_rate += 2
            elif player.walk_rate != 20: #跑速最多20
                player.walk_rate *= 2

    # update炸彈範圍
    for obj in explosions:
        obj.update1()

    # Draw things on the screen
    for obj in all_sprites:
        screen.blit(obj.surf, obj.rect)

    # 畫能量條
    for player in players:
        player.draw(screen)

    # 炸彈容量圖
    pygame.draw.rect(screen,  (212, 110, 110), (10, 10, 200, 100), 2)
    pygame.draw.rect(screen,  (212, 110, 110), (1090, 10, 200, 100), 2)
    bomb_capcity1 = pygame.font.SysFont("simhei", 25)
    text1 = bomb_capcity1.render("player1 bomb number:", True, (0, 108, 224), (0,0,0))
    screen.blit(text1, (12, 12))
    for i in range(player1.bomb_num):
        head = pygame.image.load('道具包\炸彈.png')
        screen.blit(head, (15+40*i, 60))
    bomb_capcity2 = pygame.font.SysFont("simhei", 25)
    text2 = bomb_capcity1.render("player2 bomb number:", True, (0, 108, 224), (0,0,0))
    screen.blit(text2, (1092, 12))
    for i in range(player2.bomb_num):
        head = pygame.image.load('道具包\炸彈.png')
        screen.blit(head, (1095+40*i, 60))

    # 炸彈充能時間圖
    pygame.draw.rect(screen,  (115, 115, 115), (15, 30, 180, 20), 2)
    pygame.draw.rect(screen,  (245, 43, 2), (17, 32, (player1.get_bomb_timer - player1.get_bomb_start)*176//player1.bomb_rate, 18), 0)
    pygame.draw.rect(screen,  (115, 115, 115), (1095, 30, 180, 20), 2)
    pygame.draw.rect(screen,  (245, 43, 2), (1097, 32, (player2.get_bomb_timer - player2.get_bomb_start)*176//player2.bomb_rate, 18), 0)

    # 載入圖片
    player1.anim(cmkuan)
    player2.anim(kp)
    for mine in mines:
        if not mine.invisible:
            mine.anim()
    for bomb in bombs:
        bomb.anim()
    for morepower in morepowers:
        morepower.anim()
    for faster in fasters:
        faster.anim()
    # 地圖載入圖片 
    for wood in woods:
        wood.anim()
    for rock in roros:
        rock.anim()

    # 縮圈     
    shrink_circle(radius, circle_center, screen, timer) #綠圈是下次縮圈範圍
    eliminate(player1, player2, radius, circle_center)
    radius = change_radius(radius, timer)

    # 縮圈倒數圖
    pygame.draw.rect(screen,  (212, 110, 110), (10, 200, 230, 100), 2)
    bomb_capcity1 = pygame.font.SysFont("simhei", 25)
    text1 = bomb_capcity1.render("shrink circle countdown:", True, (0, 108, 224), (0,0,0))
    screen.blit(text1, (12, 210))
    pygame.draw.rect(screen,  (115, 115, 115), (15, 230, 200, 20), 2)
    pygame.draw.rect(screen,  (245, 43, 2), (17, 232, (timer*196//1000)%196, 18), 0)

    # Update the display
    pygame.display.update()

    timer += 1 #計時器加一

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)