from json.tool import main
import pygame
import sys
from pygame.locals import *
from main import *

class Card(pygame.sprite.Sprite):
    def __init__(self, x, y,width,hight,card_state,unchosen):
        self.image=pygame.image.load(unchosen)
        width,hight =self.image.get_size()
        self.image=pygame.transform.smoothscale(self.image,(300,400))
        self.rect=(x,y,width,hight)
        # 切換卡片牌面
        self.card= card_state

    def update(self,chosen):
        if self.card == 2:
            self.image1 = pygame.image.load(chosen)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1300, 650))
        pygame.display.set_caption("角色選擇")
        self.clock = pygame.time.Clock()
        self.card4=pygame.image.load("選角畫面/鎖定按鈕.png")
        width,hight =self.card4.get_size()
        self.card4=pygame.transform.smoothscale(self.card4,(100,50))
        # 點選卡片記錄陣列
        self.click_list = []
        self.character_list=[]

    # 繪製牌子
    def set_card(self):
        card_state1 = 1
        card_state2 = 1
        card_state3 = 1

        # 卡片是否被點選
        if self.click_list == []:
            pass
        elif self.click_list[-1] == 1:
            card_state1 = 2
            card_state2 = 1
            card_state3 = 1
        elif self.click_list[-1] == 2:
            card_state2 = 2
            card_state1 = 1
            card_state3 = 1
        elif self.click_list[-1] == 3:
            card_state1 = 1
            card_state2 = 1
            card_state3 = 2
            
        x1, y1 = 150,100
        x2, y2 = 500,100
        x3, y3 = 850,100
        width1,hight1=300,400
        width2,hight2=300,400
        width3,hight3=300,400
        if card_state1 == 1:
            card1 = Card(x1, y1, width1,hight1,card_state1,"選角畫面\柯p選角.png")
        elif card_state1 == 2:
            card1 = Card(x1, y1,width1,hight1, card_state1,"選角畫面\柯p選角被選.png")
        if card_state2 == 1:
            card2 = Card(x2, y2, width2,hight2,card_state2,"選角畫面\館爺選角.png")
        else:
            card2 = Card(x2, y2, width2,hight2,card_state2,"選角畫面\館爺選角被選.png")
            
        if card_state3 == 1:
            card3 = Card(x3, y3,width2,hight2, card_state3,"選角畫面\大笨鳥選角.png")
        else:
            card3 = Card(x3, y3, width3,hight3,card_state3,"選角畫面\大笨鳥選角被選.png")
        
        self.screen.blit(card1.image, card1.rect)
        self.screen.blit(card2.image, card2.rect)
        self.screen.blit(card3.image, card3.rect)
        
        pygame.display.update()
        
 
    def lock_button(self): #鎖定角色
        # card4=pygame.image.load("選角畫面\鎖定按鈕.png")
        # width,hight =card4.get_size()
        # card4=pygame.transform.smoothscale(card4,(100,50))
        # card4.rect=(600,550,width,hight)
        self.screen.blit(self.card4, (600, 550))

    def lock_click(self, mosx, mosy):
        if len(self.character_list)<2:
            if (mosx >= 600 and mosx <= (700)) and (mosy >= 550 and mosy <= (600)):
                player=self.click_list[-1]
                self.character_list.append(player)

        if len(self.character_list)==2:
            game(self.character_list[0], self.character_list[1])


        

    # 計算滑鼠點選卡片
    def mouse_card(self, mosx, mosy):

        if (mosx >= 150 and mosx <= (450)) and (mosy >= 50 and mosy <= (545)):
            self.click_list.append(1)
        if (mosx >= 500 and mosx <= (800)) and (mosy >= 50 and mosy <= (545)):
            self.click_list.append(2)
        if (mosx >= 850 and mosx <= (1150)) and (mosy >= 50 and mosy <= (545)):
            self.click_list.append(3)
        
        
            
        

    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    mosx, mosy = event.pos
                    self.mouse_card(mosx, mosy)
                    self.lock_click(mosx, mosy)
            
            
            
            self.set_card()
            self.lock_button()
            pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()
