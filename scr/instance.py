from tkinter import Canvas
from tkinter import Label

from scr.player import Player

class  Instance():
    def __init__(self, frame=None, name=None, master=None, x=16, y=16):
        self.frame = frame
        self.name = name
        self.master = master
        self.x = x
        self.y = y
        
        text_name_map = Label(self.frame,
                              text=self.name)
        self.map = Canvas(self.frame,
                          width=self.x*10,
                          height=self.y*10,
                          background='white')
        
        text_name_map.pack()
        self.map.pack()
        
        self.loadchunk("./save/"+self.name+"/map/map.txt")
        
        self.player = Player(self.map,
                             self.hidbox,
                             self.master)
    
    def loadchunk(self, name):
        with open(name, "r") as file:
            self.mapload = []
            self.hidbox = []
            for py, line in enumerate(file.readlines()):
                self.mapload.append([])
                for px, ground in enumerate(line):
                    if ground == "o":
                        self.mapload[py].append(self.map.create_rectangle(px*10,
                                                                          py*10,
                                                                          px*10+10,
                                                                          py*10+10,
                                                                          fill="black",
                                                                          width=0))
                        self.hidbox.append((px, py))
                    
                    else:
                        self.mapload[py].append(None)
