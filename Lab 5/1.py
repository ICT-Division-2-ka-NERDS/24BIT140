import random

odd_li=[]
even_li=[]
li=[]

for i in range(5):
    odd_li.append(random.randrange(1,100,2))
for i in range(4):
    even_li.append(random.randrange(2,100,2))

odd_li.insert(3,even_li)
print("Inserted even list in odd:",odd_li)

for i in odd_li:
    if type(i)==list:
        li.extend(i)
    else:
        li.append(i)
print("Flattened list:",li)
print("Sorted flattened list",sorted(li))