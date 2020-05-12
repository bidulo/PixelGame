from tkinter import Button
from tkinter import Frame
from tkinter import Radiobutton
from tkinter import IntVar
from tkinter import Entry
from tkinter import StringVar


from os import listdir
from os import mkdir

from shutil import rmtree

from json import*

from scr.generator import CreationMap
from scr.instance import Instance

def cleanframe(frame):
    for widget in frame.winfo_children():
            widget.destroy()

def returnbutton(frame, func):
    button_return = Button(frame, text="Return", command=func)
    button_return.pack()

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.frame = Frame(master,
                           bg="black")
        
        self.frame.pack()
        
        self.home()
    
    def home(self):
        cleanframe(self.frame)
        
        button_game = Button(self.frame,
                             text="Game",
                             command=self.gameoption)
        button_quit = Button(self.frame,
                             text="Quit",
                             command=self.master.destroy)
        
        button_game.pack()
        button_quit.pack()
        
    def gameoption(self):
        cleanframe(self.frame)
        
        button_resumegame = Button(self.frame,
                                   text="List Game",
                                   command=self.listgameoption)
        button_newgame = Button(self.frame,
                                text="New Game",
                                command=self.newgameoption)
        
        button_resumegame.pack()
        button_newgame.pack()
        
        returnbutton(self.frame,
                     self.home)
    
    def listgameoption(self):
        cleanframe(self.frame)  
        
        self.variable = IntVar()
        list_map = []
        for number_map, name_map in enumerate(listdir("./save")):
            list_map.append(Radiobutton(self.frame,
                                        text=name_map,
                                        variable=self.variable,
                                        value=number_map))
            list_map[number_map].pack()
            
        button_play = Button(self.frame,
                             text="Play",
                             command=self.playgame)
        button_delete = Button(self.frame,
                               text="Delete",
                               command=self.deletegame)
        
        button_play.pack()
        button_delete.pack()
        
        returnbutton(self.frame,
                     self.gameoption)
    
    def playgame(self):
        cleanframe(self.frame)
        returnbutton(self.frame,
                     self.home)
        
        if len(listdir("./save")) == 0:
            self.listgameoption()
            return
        
        for number_map, name_map in enumerate(listdir("./save")):
            if number_map == self.variable.get():
                name_play_map = name_map
        
        game = Instance(self.frame,
                        name_play_map,
                        self.master)
    
    def deletegame(self):
        cleanframe(self.frame)
        
        if len(listdir("./save")) == 0:
            self.listgameoption()
            return
        
        for number_map, name_map in enumerate(listdir("./save")):
            if number_map == self.variable.get():
                name_delete_map = name_map
        
        rmtree("./save/"+name_delete_map)
        
        self.listgameoption()
    
    def newgameoption(self):
        cleanframe(self.frame)
        
        self.name_new_map = StringVar()
        
        entry_name_map = Entry(self.frame,
                               textvariable=self.name_new_map,
                               width=30)
        button_create = Button(self.frame,
                               text="Create",
                               command=self.newgame)
        
        entry_name_map.pack()
        button_create.pack()
        
        returnbutton(self.frame,
                     self.gameoption)
    
    def newgame(self):
        cleanframe(self.frame)
        returnbutton(self.frame,
                     self.home)
        
        if "save" not in listdir("./"):
            mkdir("./save")
        
        for number_map, list_name_map in enumerate(listdir("./save")):
            if self.name_new_map.get() in list_name_map:
                self.newgameoption()
                return
        
        create_map = CreationMap(self.frame,
                                 self.name_new_map.get(),
                                 self.master)
