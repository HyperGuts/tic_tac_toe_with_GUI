# -*- coding: utf-8 -*-

#-------------------------------
#import threading
#import time
#import itertools
import PySimpleGUI as sg
import GUI

BOARD_W = None
global firstComputerMove
firstComputerMove = True

player = 'O'
bot = 'X'

'''
def bot_opening_thread(thread_name, run_freq,  window):
         
    window.write_event_value(thread_name,'')

def gui_thread(thread_name,run_freq, window):
    for i in itertools.count():                            
        time.sleep(run_freq/1000)     
    window.write_event_value(thread_name,'')
'''    

def update_board(name,btn):
    if name=='X':
        BOARD_W[str(btn)].Update(name,disabled=True,button_color=("#FFFFFF","#303030"))
    elif name=='O':
        BOARD_W[str(btn)].Update(name,disabled=True,button_color=("#FFFFFF","#E66730"))
    
def disable_board(sw):
    for i in range(1,10):
        if BOARD_W[str(i)].get_text()=='':
            BOARD_W[str(i)].Update(disabled=sw)


def alert(msg):
    
    ALERT_W=GUI.init_alert_w(msg)
    while True:
        EVENT,VALUE=ALERT_W.Read()
    
        if EVENT is sg.WINDOW_CLOSED:
            break
        if EVENT == '-ok-' :
            
            ALERT_W.close()
            ALERT_W=None
            break
#----------------------------------------

'''def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")
'''


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    global BOARD_W
    if spaceIsFree(position):
        board[position] = letter
        #printBoard(board)
        if (checkDraw()):
            alert('Draw!')
            BOARD_W.close()
            
            
        if checkForWin():
            ###disable_board(True)
            if letter == 'X':
                alert('Bot wins!')
                BOARD_W.close()
                
            else:
                alert('Player wins!')
                BOARD_W.close()
                

        return


''' else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return
'''

def checkForWin():
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[5] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove(position):
    #position = int(input("Enter the position for 'O':  "))
    update_board('O',str(position))
    insertLetter(player, position)
    
    return


def compMove():
    disable_board(True)
    if not checkForWin():
        bestScore = -800
        bestMove = 0
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key
        update_board('X',bestMove)            
        insertLetter(bot, bestMove)
    disable_board(False)    
    
    return


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
'''
printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
'''



#global firstComputerMove


'''
while not checkForWin():
    if firstComputerMove :
        compMove()
        playerMove()
    else:
        playerMove()
        compMove()
'''
def run_options():
    
    global firstComputerMove
    
    OPTIONS_W = GUI.init_options_w(firstComputerMove)
    
    while True:
        EVENT,VALUE=OPTIONS_W.Read()
        if EVENT is sg.WINDOW_CLOSED:
            OPTIONS_W.hide()
            OPTIONS_W.close()
            OPTIONS_W=None
            break
       
        if EVENT == '-Back-':
            firstComputerMove = VALUE['-Bot-']
            break
    OPTIONS_W.close()
    OPTIONS_W=None
            
def run_game():
    global BOARD_W
    start=False 
    
    
    BOARD_W = GUI.init_game_board()
    
    global board
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    if firstComputerMove:
            start=True
    while True:
      
        if start:
            BOARD_W.finalize()
            compMove()
            start=False
        
        EVENT,VALUE=BOARD_W.Read()
        
        if EVENT is sg.WINDOW_CLOSED:
                break
      
        if EVENT in ['1','2','3','4','5','6','7','8','9'] :             
                        playerMove(int(EVENT))
                        if not (checkDraw() or checkForWin()):
                            compMove()
    BOARD_W.close()
    BOARD_W=None



def run_menu():
    
    
    MENU_W = GUI.init_menu_w()
    
    while True:
        EVENT,VALUE=MENU_W.Read()
    
        if EVENT in (sg.WINDOW_CLOSED,'-Exit-'):
            MENU_W.close()
            MENU_W=None
            break    
        if EVENT == '-Start-':
            MENU_W.close()
            MENU_W=None
            run_game()
            
           
            MENU_W = GUI.init_menu_w()
        if EVENT == '-Options-':
            run_options()
            
            #WINDOW=None
            #WINDOW = GUI.init_menu_w()
        
    
    MENU_W=None
    
'''
WINDOW = init_game_board()
run_game()
 '''       
run_menu()
        