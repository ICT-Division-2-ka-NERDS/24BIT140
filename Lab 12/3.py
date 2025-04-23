class Solid:
    def __init__(self):
        pass
    def surfaceArea(self):
        pass
    def volume(self):
        pass

class Cube(Solid):
    def __init__(self, side):
        self.side=side
    def surfaceArea(self):
        return 6*self.side**2
    def volume(self):
        return self.side**3

class Cuboid(Solid):
    def __init__(self, l, b, h):
        self.l=l
        self.b=b
        self.h=h
    def surfaceArea(self):
        return 2*((self.l*self.b)+(self.b*self.h)+(self.h*self.l))
    def volume(self):
        return self.l*self.b*self.h

solid=Cube(5)
print("Volume and surface area of the cube:")
print(solid.volume(), solid.surfaceArea(), sep=",")

solid2=Cuboid(5, 4, 3)
print("Volume and surface area of the cuboid:")
print(solid2.volume(), solid2.surfaceArea(), sep=",")
