from tkinter import Canvas

from threading import Thread

from time import sleep

from scr.instance import Instance
import scr.entity

class Player():
    def __init__(self, master=None, frame=None, name_map=None, px=0, py=0):
        self.master = master
        self.frame = frame
        self.name_map = name_map
        self.px = px
        self.py = py
        
        self.thread = Thread()
        self.instance = Instance(self.frame,
                                 self.name_map)
       
        self.is_start = False
        
        self.loadplayer()
        
        self.master.bind("<Up>",
                         self.up)
        self.master.bind("<Down>",
                         self.down)
        self.master.bind("<Right>",
                         self.right)
        self.master.bind("<Left>",
                         self.left)
        
    def loadplayer(self):
        self.chunk_x = int(self.chunkx())
        self.chunk_y = int(self.chunky())
        
        self.instance.loadchunk(self.chunk_x,
                                self.chunk_y)
        
        self.player = self.instance.map.create_rectangle((self.px%16+16)*10,
                                                         (self.py%16+16)*10,
                                                         (self.px%16+16)*10+10,
                                                         (self.py%16+16)*10+10,
                                                         fill="red",
                                                         width=0)
    
    def cooldown(func):
        def wrapper(self, event):
            if self.is_start == True:
                return
            else:
                self.thread._target = func(self, event)
                self.thread.start()
        return wrapper
    
    #@cooldown
    def up(self, event):
        self.is_start = True
        self.py -= 1
        if (self.px, self.py) in self.instance.hidbox:
            self.py += 1
            return
        self.thread._started.wait(1)
        if (1+self.py)%16 != 0:
            self.instance.map.move(self.player,
                                   0,
                                   -10)
            print (self.py , self.px)
            self.is_start = False
            return
        elif (1+self.py)%16 == 0:
            self.loadplayer()
            print (self.py , self.px)
            self.is_start = False
            return
    
    def down(self, event):
        self.py += 1
        if (self.py)%16 != 0:
            if (self.px, self.py) in self.instance.hidbox:
                self.py -= 1
                return
            self.instance.map.move(self.player,
                                   0,
                                   10)
            print (self.py , self.px)
            return
        
        elif (self.py)%16 == 0:
            if (self.px, self.py) in self.instance.hidbox:
                self.py -= 1
                return
            self.loadplayer()
            print (self.py , self.px)
    
    def right(self, event):
        self.px += 1
        if (self.px)%16 != 0:
            if (self.px, self.py) in self.instance.hidbox:
                self.px -= 1
                return
            self.instance.map.move(self.player,
                                   10,
                                   0)
            print (self.py , self.px)
            return
        
        elif (self.px)%16 == 0:
            if (self.px, self.py) in self.instance.hidbox:
                self.px -= 1
                return
            self.loadplayer()
            print (self.py , self.px)
    
    def left(self, event):
        self.px -= 1
        if (1+self.px)%16 != 0:
            if (self.px, self.py) in self.instance.hidbox:
                self.px += 1
                return
            self.instance.map.move(self.player,
                                   -10,
                                   0)
            print (self.py , self.px)
            return
        
        elif (1+self.px)%16 ==0:
            if (self.px, self.py) in self.instance.hidbox:
                self.px += 1
                return
            self.loadplayer()
            print (self.py , self.px)
    
    def chunkx(self):
        return (self.px-(self.px%16))/16
    
    def chunky(self):
        return (self.py-(self.py%16))/16
