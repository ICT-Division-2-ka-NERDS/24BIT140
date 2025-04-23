a=float(input("Enter first number"))
b=float(input("Enter second number"))
c=float(input("Enter Third number"))
if (a>b) and (a>c):
    if (b>c):
        print("Largest number is",a)
        print("Smallest number is",c)
    else:
        print("Largest number is",a)
        print("Smallest number is",b)
elif (b>a) and (b>c):
    if (a>c):
        print("Largest number is",b)
        print("Smallest number is",c)
    else:
        print("Largest number is",b)
        print("Smallest number is",a)
else:
    if (a>b):
        print("Largest number is",c)
        print("Smallest number is",b)
    else:
        print("Largest number is",c)
        print("Smallest number is",a)
        


