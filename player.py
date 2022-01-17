import pygame
import random
from pygame.locals import *

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
        if pressed_keys[K_x] and self.energy == 5 and self.at_center():
            mine = Mine(self.rect.center[0], self.rect.center[1], self)
            all_sprites.add(mine)
            mines.add(mine)
            self.energy = 0
        # 刀
        if pressed_keys[K_f] and self.energy == 5:
            knife = Knife(self.rect.center[0], self.rect.center[1], self, self.dirct)
            all_sprites.add(knife)
            knives.add(knife)
            self.energy = 0

    def update2(self, pressed_keys): #player2
        if self.at_center() or self.dirct == (0, 0):
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
        if pressed_keys[K_RALT] and self.energy == 5 and self.at_center():
            mine = Mine(self.rect.center[0], self.rect.center[1], self)
            all_sprites.add(mine)
            mines.add(mine)
            self.energy = 0

        # 刀
        if pressed_keys[K_SLASH] and self.energy == 5:
            knife = Knife(self.rect.center[0], self.rect.center[1], self, self.dirct)
            all_sprites.add(knife)
            knives.add(knife)
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