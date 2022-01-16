import pygame
import sys
import main
from pygame.locals import *
import easygui as g
import choose
import traceback

pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650


sys.setrecursionlimit(2000)
my_font = pygame.font.SysFont("arial", 16)
account = 0
account_list = 0

def log_in(account_list):
    fields = ('使用者名稱：', '密碼：')
    msg = '請輸入使用者名稱和密碼'
    title = '登入'
    user = g.multpasswordbox(msg, title, fields)
    
    if user==None:
        return "取消登入"
    elif user == ['', '']:
        button_choices=g.buttonbox('您尚未註冊，系統將不會儲存您的結果！！！','玩家', choices=('確定','註冊'))
        if button_choices=='確定':
            return 2
        elif button_choices=='註冊':
            return 1
    else:
        # 將使用者名稱讀取在list1中
        list1 = []
        Account = open('使用者名稱.txt','r')
        for each_line in Account:
            (account1, next_account) = each_line.split('\n')
            list1.append(account1)
        Account.close()

        # 將密碼讀取在list2中
        list2 = []
        Password = open('使用者密碼.txt','r')
        for each_line in Password:
            (password1, next_password) = each_line.split('\n')
            list2.append(password1)
        Password.close()

        # 確認使用者名稱和密碼是否存在並且匹配
        for X in list1:
            if X == str(user[0]) and list2[list1.index(X)] != str(user[1]):
                g.msgbox('密碼錯誤，請重新輸入!', ok_button='確定 ')
                return 0
                break
            elif X == str(user[0]) and list2[list1.index(X)] == str(user[1]):
                g.msgbox(str(user[0]) + '請選擇您要的角色!', ok_button='進入 ')
                account=list1.index(X)
                return 2
                break
        if str(user[0]) not in list1:
            g.msgbox('帳號不存在，請註冊：', ok_button='確定 ')
            return 1
            
def sign_up():
    values = []
    def create():
        msg = '*為必填項'
        title = '賬號中心'
        fields = ['*使用者名稱', '*密碼']
        return g.multenterbox(msg, title, fields, values)

    status = create()
    if status == None:
        return "取消註冊"
    else:
        while status[0] == '' or status[1] == '':
            g.msgbox('使用者名稱或密碼不能為空！', ok_button='繼續填寫 ')
            values = [status[0], status[1], status[2]]
            status = create()

        # 檢驗使用者名稱是否被佔用
        list3 = []
        Account = open('使用者名稱.txt','r')
        for each_line in Account:
            (account1, next_account) = each_line.split('\n')
            list3.append(account1)
        Account.close()
        while str(status[0]) in list3:
            g.msgbox('該使用者名稱已使用！', ok_button='重新輸入 ')
            status = create()
        # 將賬號密碼分別儲存在兩個txt檔案內
        Account = open('使用者名稱.txt', 'a')
        Account.write(status[0] + '\n')
        Account.close()
        MiMa = open('使用者密碼.txt', 'a')
        Password.write(status[1] + '\n')
        Password.close()
    
        return 0
        
def _main():
    # 建立兩個txt，分別存放使用者名稱和密碼
    Account = open('使用者名稱.txt', 'a')
    Password = open('使用者密碼.txt', 'a')
    Account.close()
    Password.close()
    
    while True:
        account_list=[]
        Account = open('使用者名稱.txt','r')
        for each_line in Account:
            (account1, next_account) = each_line.split('\n')
            account_list.append(account1)
        Account.close()

        choices = ['已有賬號，直接登入', '開始註冊']
        choice = 0
        choice = g.indexbox('登入/註冊：', '請選擇：', choices=choices)
        # 登入
        if choice==0:
            choice = log_in(account_list)
            
        # 註冊
        if choice == 1:
            choice = sign_up()
            if choice == 0:
                # 註冊成功重新切入登入頁面
                account_list=[]
                Account=open('使用者名稱.txt','r')
                for each_line in Account:
                    (account1, next_account) = each_line.split('\n')
                account_list.append(account1)
                Account.close()
                choice = log_in(account_list)
        



def choose_hero(level):

    bg_size = width,height = 1000,650
    screen = pygame.display.set_mode(bg_size)
    screen.fill((237,237,237))
    pygame.draw.rect(screen, (0,0,0), [25,100,200,200],5)
    pygame.draw.rect(screen, (0,0,0), [275,100,200,200],5)
    pygame.draw.rect(screen, (0,0,0), [525,100,200,200],5)
    pygame.draw.rect(screen, (0,0,0), [775,100,200,200],5)

    pygame.draw.rect(screen,(0,0,0),[500,550,100,50],5)
    s_font1=pygame.font.SysFont("times",34)
    s_font2=pygame.font.SysFont('ヒラキノ明朝pron',16)
    
    s_text1=s_font1.render("Hero1",True,(0,0,0))
    s_text2=s_font1.render("Hero2",True,(0,0,0))
    s_text3=s_font1.render("Hero3",True,(0,0,0))
    s_text4=s_font1.render("Hero4",True,(0,0,0))
    s_text5=s_font2.render("Confirm",True,(0,0,0))
  
    screen.blit(s_text1,(75,350))
    screen.blit(s_text2,(325,350))
    screen.blit(s_text3,(575,350))
    screen.blit(s_text4,(825,350))
    screen.blit(s_text5,(525,560))
    
    pygame.display.flip()

def _interface():
    bg_size = width,height = 1000,650
    screen = pygame.display.set_mode(bg_size)
    screen.fill((255,255,255))
    level = 1
    choose_hero(level)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 25<event.pos[0]<225 and 100<event.pos[1]<300:
                        pygame.draw.rect(screen, (25,25,25), [25,100,200,200],5)
                    elif 275<event.pos[0]<475 and 100<event.pos[1]<300:
                        pygame.draw.rect(screen, (25,25,25), [275,100,200,200],5)
                    elif 525<event.pos[0]<725 and 100<event.pos[1]<300:
                        pygame.draw.rect(screen, (25,25,25), [525,100,200,200],5)
                    elif 775<event.pos[0]<975 and 100<event.pos[1]<300:
                        pygame.draw.rect(screen, (25,25,25), [775,100,200,200],5)
                    elif 500<event.pos[0]<600 and 550<event.pos[1]<600:
                        mai.player(level)


if __name__ == '__main__':
    _main()




