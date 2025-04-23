import random

li=[]
for i in range(30):
    li.append(random.randint(-100,100))

posli=[]
negli=[]

for i in li:
    if i>0:
        posli.append(i)
    elif i<0:
        negli.append(i)

print("Positive number list:",posli)
print("Negative number list:",negli)