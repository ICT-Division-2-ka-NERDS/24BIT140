import math

class Shape:
	def __init__(self):
		pass
	def perimeter(self):
		pass
	def area(self):
		pass
	
class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	def perimeter(self):
		return 2 * math.pi * self.radius
	def area(self):
		return math.pi * self.radius ** 2
	
class Square(Shape):
	def __init__(self, side):
		self.side = side
	def perimeter(self):
		return 4 * self.side
	def area(self):
		return self.side ** 2
	
class Triangle(Shape):
	def __init__(self, side):
		self.side = side
	def perimeter(self):
		return 3 * self.side
	def area(self):
		return (math.sqrt(3) / 4) * self.side ** 2
	
circle = Circle(5)
print("Circle:")
print("Perimeter (Circumference):", circle.perimeter())
print("Area:", circle.area())
square = Square(4)
print("Square:")
print("Perimeter:", square.perimeter())
print("Area:", square.area())
triangle = Triangle(6)
print("Equilateral Triangle:")
print("Perimeter:", triangle.perimeter())
print("Area:", triangle.area())
