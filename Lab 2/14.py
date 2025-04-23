m1=float(input("Enter marks of first subject"))
m2=float(input("Enter marks of second subject"))
m3=float(input("Enter marks of third subject"))
total=m1+m2+m3
avg=total/3
print("Your total of three subjects is",total)
print("Your average of three subjects is",avg)

if 0 <= m1 <= 39:
    print("Subject 1 Grade: F")
elif 40 <= m1 <= 44:
    print("Subject 1 Grade: P")
elif 45 <= m1 <= 49:
    print("Subject 1 Grade: C")
elif 50 <= m1 <= 54:
    print("Subject 1 Grade: B")
elif 55 <= m1 <= 59:
    print("Subject 1 Grade: B+")
elif 60 <= m1 <= 69:
    print("Subject 1 Grade: A")
elif 70 <= m1 <= 79:
    print("Subject 1 Grade: A+")
elif 80 <= m1 <= 100:
    print("Subject 1 Grade: O")
else:
    print("Subject 1 Grade: NA")  

if 0 <= m2 <= 39:
    print("Subject 2 Grade: F")
elif 40 <= m2 <= 44:
    print("Subject 2 Grade: P")
elif 45 <= m2 <= 49:
    print("Subject 2 Grade: C")
elif 50 <= m2 <= 54:
    print("Subject 2 Grade: B")
elif 55 <= m2 <= 59:
    print("Subject 2 Grade: B+")
elif 60 <= m2 <= 69:
    print("Subject 2 Grade: A")
elif 70 <= m2 <= 79:
    print("Subject 2 Grade: A+")
elif 80 <= m2 <= 100:
    print("Subject 2 Grade: O")
else:
    print("Subject 2 Grade: NA")

if 0 <= m3 <= 39:
    print("Subject 3 Grade: F")
elif 40 <= m3 <= 44:
    print("Subject 3 Grade: P")
elif 45 <= m3 <= 49:
    print("Subject 3 Grade: C")
elif 50 <= m3 <= 54:
    print("Subject 3 Grade: B")
elif 55 <= m3 <= 59:
    print("Subject 3 Grade: B+")
elif 60 <= m3 <= 69:
    print("Subject 3 Grade: A")
elif 70 <= m3 <= 79:
    print("Subject 3 Grade: A+")
elif 80 <= m3 <= 100:
    print("Subject 3 Grade: O")
else:
    print("Subject 3 Grade: NA")