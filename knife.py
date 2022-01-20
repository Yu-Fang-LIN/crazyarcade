import pygame
import random
from pygame.locals import *
class Knife(pygame.sprite.Sprite):
    def __init__(self, x, y, owner, direct):
        super(Knife, self).__init__()
        self.start = pygame.time.get_ticks() #knife_timer
        self.timer = pygame.time.get_ticks()
        self.owner = owner
        self.direct = direct
        if self.direct == (0, 0):
            self.surf = pygame.Surface((40, 10))
            self.rect = self.surf.get_rect(center = (x+40, y, ))
        elif self.direct[0] > 0:
            self.surf = pygame.Surface((40, 10))
            self.rect = self.surf.get_rect(center = (x+40, y, ))
        elif self.direct[0] < 0:
            self.surf = pygame.Surface((40, 10))
            self.rect = self.surf.get_rect(center = (x-40, y, ))
        elif self.direct[1] > 0:
            self.surf = pygame.Surface((10, 40))
            self.rect = self.surf.get_rect(center = (x, y+40, ))
        elif self.direct[1] < 0:
            self.surf = pygame.Surface((10, 40))
            self.rect = self.surf.get_rect(center = (x, y-40, ))
        self.surf.fill((145, 161, 149))
        self.start = pygame.time.get_ticks() #拿到的時間
        self.timer = pygame.time.get_ticks()
    def anim(self, screen):
        if not self.owner.still:
            self.rect.move_ip(self.owner.dirct[0], self.owner.dirct[1])
        self.timer += 1
        if self.timer - self.start > 10:
            self.kill()
        if self.direct == (0, 0):
            head = pygame.image.load('道具包\刀子.png')
            head1 = pygame.transform.smoothscale(head, (10, 40))
            head2 = pygame.transform.rotate(head1, 270)
            screen.blit(head2, (self.rect.x, self.rect.y))
        elif self.direct[0] > 0:
            head = pygame.image.load('道具包\刀子.png')
            head1 = pygame.transform.smoothscale(head, (10, 40))
            head2 = pygame.transform.rotate(head1, 270)
            screen.blit(head2, (self.rect.x, self.rect.y))
        elif self.direct[0] < 0:
            head = pygame.image.load('道具包\刀子.png')
            head1 = pygame.transform.smoothscale(head, (10, 40))
            head2 = pygame.transform.rotate(head1, 90)
            screen.blit(head2, (self.rect.x, self.rect.y))
        elif self.direct[1] > 0:
            head = pygame.image.load('道具包\刀子.png')
            head1 = pygame.transform.smoothscale(head, (10, 40))
            head1 = pygame.transform.smoothscale(head, (10, 40))
            head2 = pygame.transform.rotate(head1, 180)
            screen.blit(head2, (self.rect.x, self.rect.y))
        elif self.direct[1] < 0:
            head = pygame.image.load('道具包\刀子.png')
            head1 = pygame.transform.smoothscale(head, (10, 40))
            screen.blit(head1, (self.rect.x, self.rect.y))