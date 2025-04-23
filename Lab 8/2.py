import random

s=set()
for i in range(10):
    num=random.randint(15,45)
    s.add(num)
print(s)

count=0
for i in s.copy():
    if i<30:
        count+=1

    if i>35:
        s.discard(i)

print("Values less than 30:",count)
print(s)