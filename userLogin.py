from turtle import circle
import pygame
import random
from pygame.locals import *
from Shrinkcircle import *
# from main import *
import sys
import time
from choose_charaster_test import *

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
SLATEGRAY = (121,205,205)
DODGERBLUE = (30,144,255)
DARKBLUE = (19,64,116)
CRIMSON = (220,20,60)
DARKRED = (162,44,41)
TEALBLUE = (1,111,185)
YELLOW = (230,175,46)
 
# screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SIDE_WIDTH = 300
TOTAL_WIDTH = SCREEN_WIDTH + SIDE_WIDTH

# display
MARGIN = 25
ROWS = 13
COLS = 13
CELL_SIZE = 60

# set running as global variable
running = False
done = False


class InputBox():
    def __init__(self, x, y):
        self.font = pygame.font.SysFont('Corbel',35)
        self.inputBox = pygame.Rect(x, y, 140, 32)
        self.colorInactive = WHITE
        self.colorActive = BLUE
        self.color = self.colorInactive
        self.text = ''
        self.active = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.color = self.colorActive if self.active else self.colorInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = '\n'
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.color, WHITE)
        width = max(200, 100)
        self.inputBox.w = width
        screen.blit(txtSurface, (self.inputBox.x+5, self.inputBox.y+5))
        pygame.draw.rect(screen, self.color, self.inputBox, 2)
        self.color = YELLOW


def message_display(screen, text):
    largeText = pygame.font.SysFont('freesansbold.ttf',60)
    text = largeText.render(text, True, DARKRED)
    screen.blit(text, (200, 350))
    pygame.display.update()
    time.sleep(2)

    run()

def run():
    # init account/password llist
    pygame.init()
    # initialize all screens
    w, h = SCREEN_WIDTH, SCREEN_HEIGHT
    
    global running
    # Set the height and width of the screen
    size = [TOTAL_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("crazyarcade")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    screen.blit(background, (0,0))
    pygame.display.update()
    
    # make text input boxes for accounts
    input1 = InputBox(350, 50)
    input2 = InputBox(350, 100)
    input3 = InputBox(350, 200)
    input4 = InputBox(350, 250)

    '''
    Account = open('user.txt', 'a')
    Password = open('password.txt', 'a')
    Account.close()
    Password.close()
    '''
        
    while not running:
        pygame.display.update()
        # dt = clock.tick(60)/1000
        # initiate start screen
        # startLoop(screen, start, input1, input2)
        input1.draw(screen)
        input2.draw(screen)
        input3.draw(screen)
        input4.draw(screen)
        
        account = []
        Account = open('user.txt','r')
        for each_line in Account:
            (account1, next_account) = each_line.split('\n')
            account.append(account1)
        Account.close()
        
        password = []
        Password = open('password.txt','r')
        for each_line in Password:
            (password1, next_password) = each_line.split('\n')
            password.append(password1)
        Password.close()
            
            
        quit = pygame.image.load("button/quit.png")
        login = pygame.image.load("button/login.jpg")
        create = pygame.image.load("button/signup.jpeg")
        quit = pygame.transform.smoothscale(quit,(80,80))
        login = pygame.transform.smoothscale(login,(80,80))
        create = pygame.transform.smoothscale(create,(80,80))
        quit.convert()
        login.convert()
        create.convert()
        createRect = screen.blit(create, (650, 50))
        loginRect = screen.blit(login,(650, 150))
        quitRect = screen.blit(quit, (650, 250))
        
        smallFont = pygame.font.SysFont("arial",21)
        usernameText1 = smallFont.render('Username1:', True, BLACK, YELLOW)
        passwordText1 = smallFont.render('Password1:', True, BLACK, YELLOW)
        screen.blit(usernameText1, (100, 50))
        screen.blit(passwordText1, (100, 100))
        usernameText2 = smallFont.render('Username2:', True, BLACK, YELLOW)
        passwordText2 = smallFont.render('Password2:', True, BLACK, YELLOW)
        screen.blit(usernameText2, (100, 200))
        screen.blit(passwordText2, (100, 250))
        
        for event in pygame.event.get():
            # show word
            pygame.display.update()
            
            if event.type == pygame.QUIT:
                running = True
            
            # handle textbox input
            input1.handle_event(event)
            input2.handle_event(event)
            input3.handle_event(event)
            input4.handle_event(event)
            
            # BUTTONS
            quitButton = quitRect
            createButton = createRect
            loginButton = loginRect
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                # quits game
                if quitButton.collidepoint(pos):
                    pygame.quit()
                    done = True
                    running = True
    
                # creates account
                elif createButton.collidepoint(pos):
                
                    index1 = account.index(input1.text) if input1.text in account else -1
                    index2 = account.index(input3.text) if input3.text in account else -1
                    if index1 != -1 or index2 != -1:
                        message_display(screen, 'Account aready exists')
                        # text = smallFont.render('Account aready exists', True, DARKRED)
                        # screen.blit(text, (w*.48, h*.93))
                        running = True
                        
                    else:
                        if len(input1.text) > 0 and len(input2.text) > 0 and len(input3.text) > 0 and len(input4.text) > 0 :
                            
                            Account = open('user.txt', 'a')
                            Account.write(input1.text + '\n')
                            Account.write(input3.text + '\n')
                            Account.close()
                            Password = open('password.txt', 'a')
                            Password.write(input2.text + '\n')
                            Password.write(input4.text + '\n')
                            Password.close()
                            
                            # account.append(input1.text)
                            # password.append(input2.text)
                            message_display(screen,'Created successfully')
                            # text = smallFont.render('Account Successfully Created!', True, DARKRED)
                            # screen.blit(text, (w*.48, h*.93))
                            
                        else:
                            message_display(screen,'Invalid Value')
                            # text = smallFont.render('Invalid Value', True, DARKRED)
                            # screen.blit(text, (w*.48, h*.93))
                   
                        
                # logs in and changes to profile page
                elif loginButton.collidepoint(pos):
                
                    index1 = account.index(input1.text) if input1.text in account else -1
                    index2 = account.index(input3.text) if input3.text in account else -1
                    if index1 != -1 or index2 != -1:
                        if input2.text == password[index1] and input4.text == password[index2]:
                            running = True
                            message_display(screen, 'Choose your hero')
                            # text = smallFont.render('Choose your hero!', True, DARKRED)
                            # screen.blit(text, (w*.48, h*.93))
                            G = Game()
                            G.run()
                            running = True
                            
                            # main()
                        else:
                            message_display(screen, 'Incorrect Password')
                            # text = smallFont.render('Incorrect Password', True, DARKRED)
                            # screen.blit(text, (w*.48, h*.93))
                            break
                            
                    else:
                        message_display(screen, 'Account does not exist')
                        # text = smallFont.render('Account does not exist', True, DARKRED)
                        # screen.blit(text, (w*.48, h*.93))
                        break
                        
                
        #pygame.display.flip()
        
if __name__ == "__main__":
    Account = open('user.txt', 'a')
    Password = open('password.txt', 'a')
    Account.close()
    Password.close()
    run()

