class Complex:
    def __init__(self,real,img):
        self.r=real
        self.i=img
    def printC(self):
        print(self.r,"+",self.i,"i")
    def addC(self,other):
        return Complex(self.r+other.r,self.i+other.i)
    def subC(self,other):
        return Complex(self.r-other.r,self.i-other.i)
    def mulC(self,other):
        return Complex((self.r*other.r)-(self.i*other.i),(self.r*other.i)+(self.i*other.r))
    def divC(self, other):
        denominator =other.r**2 + other.i**2
        real_part = (self.r * other.r + self.i * other.i) / denominator
        imaginary_part = (self.i * other.r - self.r * other.i) / denominator
        return Complex(real_part, imaginary_part)

ob1=Complex(10, 20)
ob2=Complex(30, 40)
ob1.printC()
ob2.printC()
print("Addition:")
ob1.addC(ob2).printC()
print("Subtraction:")
ob1.subC(ob2).printC()
print("Multiplication:")
ob1.mulC(ob2).printC()
print("Division:")
ob1.divC(ob2).printC()