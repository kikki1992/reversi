from ast import While
from email.quoprimime import body_encode
from pickle import FALSE, TRUE
from queue import Empty
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
        self.CheckBoard = self.RawBoard
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
        self.check_board = self.board.CheckBoard
        self.turn = 1
        self.row = 0
        self.col = 0
        self.check = False
        self.check_pos = self.available_pos()
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

    def available_pos(self):
        available = []
        for row in range(1,BOARD_SIZE+1):
            for col in range(1,BOARD_SIZE+1):
                #左側に反転させる石があるか
                if self.stage[row-1,col] == -self.turn:
                    row_tmp = row-2
                    col_tmp = col
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp -= 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                #右側に反転させる石があるか
                if self.stage[row+1,col] == -self.turn:
                    row_tmp = row+2
                    col_tmp = col
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp += 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                #下側に反転させる石が
                if self.stage[row,col+1] == -self.turn:
                    row_tmp = row
                    col_tmp = col + 2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        col_tmp += 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                #上側に反転させる石が
                if self.stage[row,col-1] == -self.turn:
                    row_tmp = row
                    col_tmp = col - 2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        col_tmp -= 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                #左上側に反転させる石が
                if self.stage[row-1,col-1] == -self.turn:
                    row_tmp = row-2
                    col_tmp = col - 2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp -= 1
                        col_tmp -= 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                #右上側に反転させる石があるか
                if self.stage[row+1,col-1] == -self.turn:
                    row_tmp = row+2
                    col_tmp = col - 2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp += 1
                        col_tmp -= 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                 #右下側に反転させる石があるか
                if self.stage[row+1,col+1] == -self.turn:
                    row_tmp = row+2
                    col_tmp = col+2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp += 1
                        col_tmp += 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                #左下側に反転させる石があるか
                if self.stage[row-1,col+1] == -self.turn:
                    row_tmp = row-2
                    col_tmp = col+2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp -= 1
                        col_tmp += 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue

        return available

    def put_stone(self,row,col):
        check = False
        #左側をひっくり返す
        if self.stage[row-1,col] == -self.turn:
            row_tmp = row-2
            col_tmp = col
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp -= 1
    
            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row_tmp:row+1,col_tmp] = self.turn
                check = True

        #右側をひっくり返す
        if self.stage[row+1,col] == -self.turn:
            row_tmp = row+2
            col_tmp = col
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp += 1

            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row:row_tmp+1,col_tmp] = self.turn
                check = True

        #下側をひっくり返す
        if self.stage[row,col+1] == -self.turn:
            row_tmp = row
            col_tmp = col+2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                col_tmp += 1

            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row,col:col_tmp+1] = self.turn
                check = True

        #上側をひっくり返す
        if self.stage[row,col-1] == -self.turn:
            row_tmp = row
            col_tmp = col-2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                col_tmp -= 1

            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row,col_tmp:col+1] = self.turn
                check = True

        #左下をひっくり返す
        counts = 2
        if self.stage[row-1,col+1] == -self.turn:
            row_tmp = row-2
            col_tmp = col+2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp -= 1
                col_tmp += 1
                counts += 1
            if self.stage[row_tmp,col_tmp] == self.turn:
                for i in range(counts+1):
                    self.stage[row-i,col+i] = self.turn
                check = True

        #左上をひっくり返す
        counts = 2
        if self.stage[row-1,col-1] == -self.turn:
            row_tmp = row-2
            col_tmp = col-2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp -= 1
                col_tmp -= 1
                counts += 1
            if self.stage[row_tmp,col_tmp] == self.turn:
                for i in range(counts+1):
                    self.stage[row-i,col-i] = self.turn
                check = True
        
        #右下をひっくり返す
        counts = 2
        if self.stage[row+1,col+1] == -self.turn:
            row_tmp = row+2
            col_tmp = col+2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp += 1
                col_tmp += 1
                counts += 1
            if self.stage[row_tmp,col_tmp] == self.turn:
                for i in range(counts+1):
                    self.stage[row+i,col+i] = self.turn
                check = True
              
        #右上をひっくり返す
        counts = 2
        if self.stage[row+1,col-1] == -self.turn:
            row_tmp = row+2
            col_tmp = col-2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp += 1
                col_tmp -= 1
                counts += 1
            if self.stage[row_tmp,col_tmp] == self.turn:
                for i in range(counts+1):
                    self.stage[row+i,col-i] = self.turn
                check = True

        return check


    def update(self):

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.x = pyxel.mouse_x
            self.y = pyxel.mouse_y
        
            #盤面内をクリックした場合のアクション
            if 150 < self.x < 630 and 50 < self.y < 530 :
                self.row = (self.x - 90)//60 
                self.col = (self.y +10)//60
                if self.stage[self.row,self.col] == 0:
                    self.check = self.put_stone(self.row,self.col)
                    if self.check == True:
                        self.turn *= -1
                        self.check_pos = self.available_pos()

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

        for i in self.check_pos:
            pyxel.circ(120+i[0]*60,20+i[1]*60,5,2)

        pyuni.text(0,1,"row{},col{}".format(self.row,self.col),0)
        pyuni.text(0,40,"{}".format(self.stage[self.row,self.col]),0)
        pyuni.text(0,80,"{}".format(self.check),0)

        if self.turn == 1:
            s = "BLACK"
        else:
            s = "WHITE"

        
App()


