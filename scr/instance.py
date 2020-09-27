from scr.map import Map

from scr.player import Player

class Instance():
    def __init__(self, master=None, frame=None, name_map=None):
        self.master = master
        self.frame = frame
        self.name_map = name_map
        
        self.map = Map(self.frame, 
                       self.name_map)
        self.player = Player(self.master,
                             self.frame,
                             self.map)
        
        self.player.loadplayer()