import numpy as np
import pyxel

class Board():
    def __init__(self):
        EMPTY = 0
        WHITE = -1
        BLACK = 1
        WALL = 2
        BOARD_SIZE = 8
        self.RawBoard = np.zeros((BOARD_SIZE+2, BOARD_SIZE+2),dtype=int)
        self.RawBoard[0,:] = WALL
        self.RawBoard[:,0] = WALL
        self.RawBoard[BOARD_SIZE+1,:] = WALL
        self.RawBoard[:,BOARD_SIZE+1] = WALL
        self.RawBoard[4,4] = WHITE
        self.RawBoard[5,5] = WHITE
        self.RawBoard[5,4] = BLACK
        self.RawBoard[4,5] = BLACK


class App():
    def __init__(self):
        pyxel.init(120,160,title="Reversi")
        self.board = Board()
        self.stage = self.board.RawBoard
        self.turn = 1
        self.row = 0
        self.col = 0
        self.black_count = 2
        self.white_count = 2
        self.check = False
        self.check_pos = self.available_pos()
        self.flag = 0
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

    def available_pos(self):
        EMPTY = 0
        WHITE = -1
        BLACK = 1
        WALL = 2
        BOARD_SIZE = 8
        available = []
        for row in range(1,BOARD_SIZE+1):
            for col in range(1,BOARD_SIZE+1):
                if self.stage[row-1,col] == -self.turn:
                    row_tmp = row-2
                    col_tmp = col
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp -= 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                if self.stage[row+1,col] == -self.turn:
                    row_tmp = row+2
                    col_tmp = col
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        row_tmp += 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                if self.stage[row,col+1] == -self.turn:
                    row_tmp = row
                    col_tmp = col + 2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        col_tmp += 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
                if self.stage[row,col-1] == -self.turn:
                    row_tmp = row
                    col_tmp = col - 2
                    while self.stage[row_tmp,col_tmp] == -self.turn:
                        col_tmp -= 1
                    if self.stage[row_tmp,col_tmp] == self.turn and self.stage[row,col] == EMPTY:
                        pos = [row,col]
                        available.append(pos)
                        continue
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
        if self.stage[row-1,col] == -self.turn:
            row_tmp = row-2
            col_tmp = col
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp -= 1
    
            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row_tmp:row+1,col_tmp] = self.turn
                check = True

        if self.stage[row+1,col] == -self.turn:
            row_tmp = row+2
            col_tmp = col
            while self.stage[row_tmp,col_tmp] == -self.turn:
                row_tmp += 1

            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row:row_tmp+1,col_tmp] = self.turn
                check = True

        if self.stage[row,col+1] == -self.turn:
            row_tmp = row
            col_tmp = col+2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                col_tmp += 1

            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row,col:col_tmp+1] = self.turn
                check = True

        if self.stage[row,col-1] == -self.turn:
            row_tmp = row
            col_tmp = col-2
            while self.stage[row_tmp,col_tmp] == -self.turn:
                col_tmp -= 1

            if self.stage[row_tmp,col_tmp] == self.turn:
                self.stage[row,col_tmp:col+1] = self.turn
                check = True

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
        EMPTY = 0
        WHITE = -1
        BLACK = 1
        WALL = 2
        BOARD_SIZE = 8

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.x = pyxel.mouse_x
            self.y = pyxel.mouse_y
        
            if 50 < self.x < 530 and 50 < self.y < 530 :
                self.row = (self.x + 10)//60 
                self.col = (self.y +10)//60
                if self.stage[self.row,self.col] == 0:
                    self.check = self.put_stone(self.row,self.col)
                    if self.check == True:
                        self.turn *= -1
                        self.check_pos = self.available_pos()
                        
                        self.black_count = 0
                        self.white_count = 0
                        for row in range(1,BOARD_SIZE+1):
                            for col in range(1,BOARD_SIZE+1):
                                if self.stage[row,col] == 1:
                                    self.black_count += 1
                                if self.stage[row,col] == -1:
                                    self.white_count += 1
        
            if 550 < self.x < 690 and 400 < self.y < 460 and len(self.check_pos) == 0:
                self.turn *= -1
                self.check_pos = self.available_pos()
                if len(self.check_pos) == 0:
                    self.flag =1

            if self.black_count + self.white_count == 64 or self.black_count == 0 or self.white_count == 0:
                self.flag = 1
            
            if self.flag == 1 and 170 < self.x < 410 and 310 < self.y < 390:
                self.flag = 0
                self.board = Board()
                self.stage = self.board.RawBoard
                self.turn = 1
                self.row = 0
                self.col = 0
                self.black_count = 2
                self.white_count = 2
                self.check = False
                self.check_pos = self.available_pos()
                


    def draw(self):
        EMPTY = 0
        WHITE = -1
        BLACK = 1
        WALL = 2
        BOARD_SIZE = 8
        pyxel.cls(1)
        pyxel.rect(50,50,480,480,11)
        for i in range(50,535,60):
            pyxel.line(i,50,i,530,0)
        for i in range(50,535,60):
            pyxel.line(50,i,530,i,0)
        
        for j in range(1,BOARD_SIZE+1):
            for i in range(1,BOARD_SIZE+1):
                if self.stage[i,j] == BLACK:
                    pyxel.circ(20+i*60,20+j*60,20,0)
                elif self.stage[i,j] == WHITE:
                    pyxel.circ(20+i*60,20+j*60,20,7)

        for i in self.check_pos:
            pyxel.circ(20+i[0]*60,20+i[1]*60,5,2)

        if self.turn == 1:
            s = "BLACK"
            color = 0
            B_color = 7
        else:
            s = "WHITE"
            color = 7
            B_color = 0
        
        pyxel.rect(545,45,170,100,9)
        pyxel.rect(550,50,160,90,B_color)
    
        pyxel.text(560,60,"TURN",color)
        pyxel.text(560,100,"{}".format(s),color)

        pyxel.text(560,180,"BLACK",7)
        pyxel.text(560,220,"{}".format(self.black_count),7)
        pyxel.text(560,300,"WHITE",7)
        pyxel.text(560,340,"{}".format(self.white_count),7)

        pyxel.rect(545,395,150,70,14)
        pyxel.rect(550,400,140,60,13)
        pyxel.text(560,410,"PATH",0)

        if self.flag == 1 :
            pyxel.rect(80,80,420,420,9)
            pyxel.rect(90,90,400,400,7)

            pyxel.rect(160,300,260,100,14)
            pyxel.rect(170,310,240,80,13)
            pyxel.text(200,330,"Restart",0)

            if self.white_count>self.black_count:
                pyxel.text(100,160,"WHITE Win!!",1)
            elif self.white_count<self.black_count:
                pyxel.text(100,160,"BLACK Win!!",1)
            else:
                pyxel.text(100,160,"EQUALL",1)

App()


