import random

li=[]
for i in range(10):
    li.append(random.randint(-15,15))
print(li)

sqli=list(map(lambda x: x**2, li))
print("Square of each number in list:",sqli)
