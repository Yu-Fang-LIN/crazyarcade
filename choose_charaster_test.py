
import pygame
import sys
from pygame.locals import *

class Card(pygame.sprite.Sprite):
    def __init__(self, x, y, card_state,unchosen):
        self.image=pygame.image.load(unchosen)
        width,hight =self.image.get_size()
        self.rect=(x,y,width,hight)
        
        # 切換卡片牌面
        self.card= card_state
        

    def update(self,chosen):
        if self.card == 2:
            self.image = pygame.image.load(chosen)

        
            


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("角色選擇")
        self.clock = pygame.time.Clock()
    
        # 點選卡片記錄陣列
        self.click_list = []

   


    # 繪製牌子
    def set_card(self):
        x1, y1 = 75,45
        x2, y2 = 325,45
        x3, y3 = 575,45
        card_state1 = 1
        card_state2 = 1
        card_state3 = 1
        card1 = Card(x1, y1, card_state1,"選角畫面\柯p選角.png")
        card2 = Card(x2, y2, card_state2,"選角畫面\館爺選角.png")
        card3 = Card(x3, y3, card_state3,"選角畫面\大笨鳥選角.png")
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
            card_state1 = 2
            card_state2 = 1
            card_state3 = 1
        card1.update("選角畫面\柯p選角被選.png")
        card2.update("選角畫面\館爺選角被選.png")
        card3.update("選角畫面\大笨鳥選角被選.png")
        self.screen.blit(card1.image, card1.rect)
        self.screen.blit(card2.image, card2.rect)
        self.screen.blit(card3.image, card3.rect)
        

    # 計算滑鼠點選卡片
    def mouse_card(self, mosx, mosy):

        if (mosx >= 75 and mosx <= (325)) and (mosy >= 45 and mosy <= (545)):
            self.click_list.append(1)
        if (mosx >= 325.1 and mosx <= (550)) and (mosy >= 45 and mosy <= (545)):
            self.click_list.append(2)
        if (mosx >= 575.1 and mosx <= (825)) and (mosy >= 45 and mosy <= (545)):
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

            
            self.set_card()

            pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()