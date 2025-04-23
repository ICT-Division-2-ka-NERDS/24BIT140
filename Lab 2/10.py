length=float(input("Enter length of rectangle"))
breadth=float(input("Enter width of rectangle"))
area=length*breadth
perimeter=2*(length+breadth)
if(area>perimeter):
    print("Area is greater than perimeter ")
else:
    print("Perimeter is greater than area")