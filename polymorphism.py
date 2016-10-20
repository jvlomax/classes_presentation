"""
Python uses duck typing, and polymorphism is something we don't really worry about.

If it walks like a duck, talks like a duck, quacks like a duck, we'll say it's a duck!
"""


class Person():
    def __init__(self, posx, posy, vx, vy):
        self.posx = posx
        self.posy = posy
        self.vx = vx
        self.vy = vy

    def jump(self, height=10):
        self.vx += height

if __name__ == "__main__":
    l = list()
    l.append({"Cheese": 5, "milk": 4, "bread": 2})
    l.append(3.4)
    l.append("Random string with plenty of characters")
    import time
    l.append(time.time())
    print(l)
