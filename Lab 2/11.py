x1=float(input("Enter x1 cordinate"))
y1=float(input("Enter y1 cordinate"))
x2=float(input("Enter x2 cordinate"))
y2=float(input("Enter y2 cordinate"))
x3=float(input("Enter x3 cordinate"))
y3=float(input("Enter y3 cordinate"))
m1=(y2-y1)/(x2-x1)
m2=(y3-y2)/(x3-x2)
if m1==m2:
    print("All points lies on the same line")
else:
    print("All points don't lie on the same line")