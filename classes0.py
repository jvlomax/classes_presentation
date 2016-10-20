class Entity:
    def __init__(self):
        self.posx
        self.posy
        self.vs
        self.vx

    def move(self):
        self.posx += self.vx
        self.posy = self.vy

    def update(self):
        draw_at(self.posx, self.posy)


class Player(Entity):
    pass

class Enemy(Entity):
    pass

if __name__ == "__main__":
    player = Player()
    enemy = Player()
    object = Entity()

