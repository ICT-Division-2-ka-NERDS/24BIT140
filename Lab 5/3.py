import random

li=[]
for i in range(50):
    li.append(random.randint(1,30))

uniqueli=[]

for i in li:
    if i not in uniqueli:
        uniqueli.append(i)

print("List without duplicates:",uniqueli)