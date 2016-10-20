"""
Basic inheritance
"""

class Entity:
    def __init__(self, posx, posy, vx, vy):
        self.posx = posx
        self.posy = posy
        self.vx = vx
        self.vy = vy
    
    def move(self):
        self.posx += self.vx
        self.posy += self.vy


class Player(Entity):
    def __init__(self, posx, posy, vx, vy):
        super().__init__(posx, posy, vx, vy)
        self.alive = True
    
    def jump(self):
        self.posy += 10


class Ball(Entity):
    
    def deflate():
        self.alive = False
        
player = Player(0, 0, 3, 0)
ball = Ball(20, 10, -5, -1)
player.move()
ball.move()