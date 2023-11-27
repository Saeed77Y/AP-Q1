from math import pi

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def getArea(self):
        return pow(self.radius, 2) * pi
    
    def getPerimeter(self):
        return self.radius * 2 * pi