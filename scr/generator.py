from random import randint

from os import mkdir

from scr.instance import Instance

class CreationMap():
    def __init__(self, frame=None, name=None, master=None):
        self.frame = frame
        self.name = name
        self.master = master 
        
        mkdir("./save/"+self.name)
        mkdir("./save/"+self.name+"/map")
        mkdir("./save/"+self.name+"/data")
        
        self.writechunk(self.name)
        
        game = Instance(self.frame,
                        self.name,
                        self.master)
        
    def writechunk(self, name):
        with open("./save/"+name+"/map/map.txt", "w") as file:
            for y in range(16):
                for x in range(16):
                    o = randint(0, 100)
                    if o <= 10:
                        file.write("o")
                    
                    else:
                        file.write("x")
                
                file.write("\n")