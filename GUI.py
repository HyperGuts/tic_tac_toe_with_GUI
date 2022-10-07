# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:12:26 2022

@author: szabo
"""



import PySimpleGUI as sg

#settings
RESOLUTION=(1024,600)
BTN_SIZE=(20,2)
BTN_F_SIZE=20
BG_COLOR='#303030'  #'#FFE042' 
F_COLOR='#E66730'
BB_SIZE=(3,1)
BBF_SIZE=70
#default
header = {'text':'TIC-TAC-TOE','text_color' : F_COLOR ,'background_color' : BG_COLOR,'font': ('Franklin Ghotic Book',60)}
button_style = {'size': BTN_SIZE, 'font':('Franklin Ghotic Book',BTN_F_SIZE),'button_color':("black","#FFFFFF")}
b_button_style = {'button_text':' ','size':BB_SIZE, 'font':('Franklin Ghotic Book',BBF_SIZE),'button_color':("black","#FFFFFF")}
app_window = {'size':RESOLUTION,'keep_on_top':True, 'element_justification':'c','background_color':BG_COLOR}
#Window inits
def init_menu_w():
    
    MENU_LAYOUT = [[sg.T(**header)],
                   [sg.Button(button_text='Start',**button_style,key= '-Start-' )],
                   [sg.Button(button_text='Options',**button_style,key= '-Options-' )],
                   [sg.Button(button_text='Exit',**button_style,key= '-Exit-' )]]

    return sg.Window(title='Menu',**app_window).Layout(MENU_LAYOUT)

def init_options_w(isBot):
    OPTIONS_LAYOUT = [[sg.T(**header)],
                      [sg.Frame(layout=[[sg.Radio('Player',font=('Franklin Ghotic Book',20), group_id="INIT_P",background_color=BG_COLOR, key='-Player-',default=(not isBot),
                                                     size=(20, 1)),
                                           sg.Radio('Bot',font=('Franklin Ghotic Book',20), group_id="INIT_P",background_color=BG_COLOR, key='-Bot-',default=isBot,)]],
                                  title='Choose who should start:',font=('Franklin Ghotic Book',20),background_color=BG_COLOR, relief=sg.RELIEF_GROOVE,
                                  tooltip='Set initial player')],
                      [sg.Button(button_text='Back',**button_style,key= '-Back-' )]]    

    return sg.Window('Options',**app_window).Layout(OPTIONS_LAYOUT)


def init_game_board():
   
    GAME_BOARD_LAYOUT = [[sg.Frame(layout=[[sg.Button(**b_button_style,key= str(i+j*3) ) 
                                                for i in range(1,4)] 
                                               for j in range(3)]
                                       , title='Board', relief=sg.RELIEF_GROOVE,background_color=BG_COLOR)]
                            ]
    return sg.Window(title='Tic Tac Toe',**app_window,).Layout(GAME_BOARD_LAYOUT)
    
def init_alert_w(msg):
    ALERT_LAYOUT=[[sg.T(str(msg),font=('Franklin Ghotic Book',20),text_color=F_COLOR,background_color='#505050')],[sg.Button(button_text='OK',size=(5,1), font=('Franklin Ghotic Book',10),button_color=("black","#FFFFFF"),key= '-ok-'),]]
    
    return sg.Window(title='Resoult',no_titlebar=True,modal=True, size=(300,100), keep_on_top=True, element_justification='c',background_color='#505050').Layout(ALERT_LAYOUT)


