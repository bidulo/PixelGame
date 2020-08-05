from tkinter import Canvas
from tkinter import Label

from random import randint

from os import listdir
from os import mkdir

class  Instance():
    def __init__(self, frame=None, name_map=None):
        self.frame = frame
        self.name_map = name_map
        
        text_name_map = Label(self.frame,
                              text=self.name_map)
        self.map = Canvas(self.frame,
                          width=480,
                          height=480,
                          background='white')
        
        text_name_map.pack()
        self.map.pack()

        self.hidbox = [0]
        
    def loadchunk(self, chunk_x=None, chunk_y=None):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        
        self.hidbox.pop()
        self.map.delete("all")
        
        multi = [[0, 0], [1, 0], [2, 0],
                 [0, 1], [1, 1], [2, 1],
                 [0, 2], [1, 2], [2, 2]]
        self.multi_chunk = [[-1, -1], [0, -1], [1, -1],
                            [-1, 0], [0, 0], [1, 0],
                            [-1, 1], [0, 1], [1, 1]]
        
        for v, self.name_chunk in enumerate(self.namechunk()):
            if self.name_chunk+".txt" not in listdir("./save/"+self.name_map+"/map"):
                self.generatorchunk()
            
            with open("./save/"+self.name_map+"/map/"+self.name_chunk+".txt", "r") as file:
                for py, line in enumerate(file.readlines()):
                    for px, ground in enumerate(line):
                        if ground == "o":
                            block = self.map.create_rectangle((px+16*multi[v][0])*10,
                                                              (py+16*multi[v][1])*10,
                                                              (px+16*multi[v][0])*10+10,
                                                              (py+16*multi[v][1])*10+10,
                                                              fill="black",
                                                              width=0)
                            self.hidbox.append((px+16*self.multi_chunk[v][0]+16*self.chunk_x, py+16*self.multi_chunk[v][1]+16*self.chunk_y))
    
    def namechunk(self):
        listchunk = []
        for v in range(0, 9):
            listchunk.append(str(self.chunk_x+self.multi_chunk[v][0])+"I"+str(self.chunk_y+self.multi_chunk[v][1]))
        return listchunk
    
    def generatorchunk(self):
        with open("./save/"+self.name_map+"/map/"+self.name_chunk+".txt", "w") as file:
            for y in range(16):
                for x in range(16):
                    o = randint(0, 100)
                    if o <= 10:
                        if (x, y) == (0, 0):
                            file.write("x")
                        else:
                            file.write("o")
                    
                    else:
                        file.write("x")
                
                file.write("\n")
