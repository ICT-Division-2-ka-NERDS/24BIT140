import math
xc=float(input("Enter x coordinate of center of circle:"))
yc=float(input("Enter y coordinate of center of circle:"))
r=float(input("Enter radius of circle:"))
xp=float(input("Enter x coordinate of point:"))
yp=float(input("Enter y coordinate of point:"))
distance=math.sqrt(math.pow(xp - xc, 2) + math.pow(yp - yc, 2))
if distance<r:
    print("Point is inside the circle")
elif distance==r:
    print("Point is on the circle")
else:
    print("Point is outside the circle")

