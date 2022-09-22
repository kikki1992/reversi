from ast import While
from pickle import FALSE, TRUE
from tabnanny import check
import numpy as np
import pyxel
from pyxelunicode import PyxelUnicode

# 0:空き枠、1:黒いし、-1: 白石、2:壁

EMPTY = 0
WHITE = -1
BLACK = 1
WALL = 2
BOARD_SIZE = 8

font_path = "assets/x14y20pxScoreDozer.ttf"
font_size = 40

pyuni = PyxelUnicode(font_path, font_size)

class Board():
    def __init__(self):
        self.RawBoard = np.zeros((BOARD_SIZE+2, BOARD_SIZE+2),dtype=int)
        #上の壁
        self.RawBoard[0,:] = WALL
        #左の壁
        self.RawBoard[:,0] = WALL
        #下の壁
        self.RawBoard[BOARD_SIZE+1,:] = WALL
        #右の壁
        self.RawBoard[:,BOARD_SIZE+1] = WALL
        
        #初期位置
        self.RawBoard[4,4] = WHITE
        self.RawBoard[5,5] = WHITE
        self.RawBoard[5,4] = BLACK
        self.RawBoard[4,5] = BLACK


class App():
    def __init__(self):
        #Windowの作成(最初に設定)
        pyxel.init(800,600,title="Reversi")
        self.board = Board()
        self.stage = self.board.RawBoard
        self.turn = 1
        self.row = 0
        self.col = 0
        self.check = False
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

                     
    def check_put(self,row,col):
        if self.stage[row-1,col] == self.turn*-1:
            return True
        else:
            return False


    def update(self):

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.x = pyxel.mouse_x
            self.y = pyxel.mouse_y
        
            #盤面内をクリックした場合のアクション
            if 150 < self.x < 630 and 50 < self.y < 530 :
                self.row = (self.x - 90)//60 
                self.col = (self.y +10)//60
                if self.stage[self.row,self.col] == 0:
                    self.stage[self.row,self.col] = self.turn
                    self.check = self.check_put(self.row,self.col)
                    self.turn *= -1

    def draw(self):
        pyxel.cls(1)
        pyxel.rect(150,50,480,480,11)
        for i in range(150,635,60):
            pyxel.line(i,50,i,530,0)
        for i in range(50,535,60):
            pyxel.line(150,i,630,i,0)
        
        for j in range(1,BOARD_SIZE+1):
            for i in range(1,BOARD_SIZE+1):
                if self.stage[i,j] == BLACK:
                    pyxel.circ(120+i*60,20+j*60,20,0)
                elif self.stage[i,j] == WHITE:
                    pyxel.circ(120+i*60,20+j*60,20,7)

        pyuni.text(0,1,"row{},col{}".format(self.row,self.col),0)
        pyuni.text(0,40,"{}".format(self.stage[self.row,self.col]),0)
        pyuni.text(0,80,"{}".format(self.check),0)
        
App()


