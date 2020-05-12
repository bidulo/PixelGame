from tkinter import Canvas

import scr.entity

class Player():
    def __init__(self, map, hidbox, master, px=0, py=0):
        self.map = map
        self.hidbox = hidbox
        self.master = master
        self.px = px
        self.py = py
        
        self.loadplayer()
        
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Left>", self.left)
        
    def loadplayer(self):
        if (self.px, self.py) in self.hidbox:
            self.px += 1
            self.loadplayer()
            return
        
        
        self.player = self.map.create_rectangle(self.px*10,
                                                self.py*10,
                                                self.px*10+10,
                                                self.py*10+10,
                                                fill="red",
                                                width=0)
    
    def up(self, event):
        self.py -= 1
        if self.py > -1: #condition amener a disparaitre
            if (self.px, self.py) in self.hidbox:
                self.py += 1
                return
            self.map.move(self.player,
                          0,
                          -10) 
            print (self.py , self.px)
            return
        
        if self.py <= 0: #idem
            self.py +=1
            print (self.py , self.px)
    
    def down(self, event):
        self.py += 1
        if self.py < 16:  #condition amener a disparaitre
            if (self.px, self.py) in self.hidbox:
                self.py -= 1
                return
            self.map.move(self.player,
                          0,
                          10)
            print (self.py , self.px)
            return
        
        if self.py >= 16: #idem
            self.py -= 1
            print (self.py , self.px)
    
    def right(self, event):
        self.px += 1
        if self.px < 16: #condition amener a disparaitre
            if (self.px, self.py) in self.hidbox:
                self.px -= 1
                return
            self.map.move(self.player,
                          10,
                          0)
            print (self.py , self.px)
            return
        
        if self.px >= 16: #idem
            self.px -=1
            print (self.py , self.px)
    
    def left(self, event):
        self.px -= 1
        if self.px > -1: #condition amener a disparaitre
            if (self.px, self.py) in self.hidbox:
                self.px += 1
                return
            self.map.move(self.player,
                          -10,
                          0)
            print (self.py , self.px)
            return
        
        if self.px <= 0: #idem
            self.px +=1
            print (self.py , self.px)
    
    def positionplayer(self): #pour plus tard
        return self.px, self.py