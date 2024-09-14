import pygame
import sys   
import numpy as np


pygame.init()
sw=450
sh=450

gridColour=(0,255,255)
br=3

game_over=False
bc=3
screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("TicTacToe")
screen.fill((0,0,17))

board=np.zeros((br,bc))


def draw_line():
    pygame.draw.line(screen,gridColour,(0,150),(450,150),1)
    pygame.draw.line(screen,gridColour,(0,300),(450,300),1)
    pygame.draw.line(screen,gridColour,(150,0),(150,450),1)
    pygame.draw.line(screen,gridColour,(300,0),(300,450),1)


def mark_square(row,col,player):
    board[row][col]=player

def available_square(row,column):
    return board[row][column]==0

def is_board_full():
    for row in range(br):
        for column in range(bc):
            if board[row][column]==0:
                return False
    
    return True


def vertical(col,player):
    posX=col*150 +75

    pygame.draw.line(screen,(255,255,255),(posX,15),(posX,sh-15),2)

def horizontal(row,player):
    posY=row*150+75

    pygame.draw.line(screen,(255,255,255),(15,posY),(sw-15,posY),2)

def draw_asc(player):
    pygame.draw.line(screen,(255,255,255),(15,sh-15),(sw-15,15),2)

def draw_dec(player):
    pygame.draw.line(screen,(255,255,255),(15,15),(sw-15,sh-15),2)

def restart():
    screen.fill((0,0,17))
    draw_line()
    player=1
    for row in range(br):
        for col in range(bc):
            board[row][col]=0
    game()

       

def win(player):
    for col in range(bc):
        if board[0][col]== player and board [1][col]==player and board[2][col]==player:
            horizontal(col,player)
            return True

    for row in range(br):
        if board[row][0]==player and board [row][1]==player and board [row][2]==player:
            vertical(row,player)
            return True
    
    if board[0][0]==player and board [1][1]==player and board [2][2]==player:
        draw_dec(player)
        return True
    
    
    if board[0][2]==player and board [1][1]==player and board [2][0]==player:
        draw_asc(player)
        return True





def draw_figures():
    for row in range(br):
        for col in range(bc):
            if board[row][col]  == 2:
                pygame.draw.circle(screen , (0,255,0),(int(row*150+75),int(col*150+75)),40,2) 
            elif board[row][col]==1:
                pygame.draw.line(screen,(255,0,255),(int(row*150+25),int(col*150+25)),(int(row*150+125),int(col*150+125)))
                pygame.draw.line(screen,(255,0,255),(int(row*150+25),int(col*150+125)),(int(row*150+125),int(col*150+25)))


draw_line()




def game():
    game_over=False
    player=1
    while True:
        for event in pygame.event.get():
        
            if is_board_full==True:
                sys.exit()
                
            if event.type == pygame.QUIT:
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and game_over==False:

                mouseX=int(event.pos[0]//150)
                mouseY=int(event.pos[1]//150)

                if available_square(mouseX,mouseY):
                    if player == 1:
                        mark_square(mouseX,mouseY,1)
                        draw_figures()
                        if win(player):
                            game_over=True
                        player=2
                    elif player == 2:
                        mark_square(mouseX,mouseY,2)
                        draw_figures()
                        if win(player):
                            game_over=True
                        player=1
                
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_r:
                    restart()

        pygame.display.update()

game()