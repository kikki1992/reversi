from pydoc import visiblename
import pyxel
from pyxelunicode import PyxelUnicode

init_stage = [0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,2,1,0,0,0,
        0,0,0,1,2,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,]


class App():
    def __init__(self):
        #Windowの作成(最初に設定)
        pyxel.init(800,600,title="Reversi")
        self.stage = init_stage
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

        
    def update(self):
        pass

    def draw(self):
        pyxel.cls(1)
        pyxel.rect(150,50,480,480,11)
        for i in range(150,635,60):
            pyxel.line(i,50,i,530,0)
        for i in range(50,535,60):
            pyxel.line(150,i,630,i,0)
        
        num = 0
        for i in self.stage:
            if i == 1:
                row = num % 8
                col = num // 8
                pyxel.circ(180+row*60,80+col*60,20,0)
            elif i == 2:
                row = num % 8
                col = num // 8
                pyxel.circ(180+row*60,80+col*60,20,7)
            num += 1
            

App()

