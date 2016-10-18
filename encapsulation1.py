

class Point:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x  = x
        self.y = y
        
    @property
    def area(self):
        return self.height * self.width
        
    
    
if __name__ == "__main__":
    point1 = Point(1, 1, 20, 20)
    point2 = Point(1, 1, 45, 30)
    print(point1.area)
    print(point2.area)
    