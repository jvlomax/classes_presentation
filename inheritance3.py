from abc import ABCMeta, abstractmethod

"""
Abstract classes
"""


class Entity(metaclass=ABCMeta):
    def __init__(self, posx, posy, vx, vy):
        self.posx = posx
        self.posy = posy
        self.vx = vx
        self.vy = vy
    
    @abstractmethod
    def move(self):
        pass


class Player(Entity):
 
    def move(self):
        self.posx += self.vx
        
    
if __name__ == "__main__":
    player = Player(0, 0, 10, 0)