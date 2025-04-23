import random

li=[]
for i in range(20):
    li.append(random.randint(0,100))

num=int(input("Enter a number"))
positions = [index for index, value in enumerate(li) if value == num]

if positions:
    print(num,"appears at positions",positions)
else:
    print(num,"does not appear in the list")
