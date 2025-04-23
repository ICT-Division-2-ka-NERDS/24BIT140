import random

l1 = []
l2 = []
l3 = []

for i in range(20):
    l1.append(random.randint(1, 20))
    l2.append(random.randint(1, 20))

for num in l1:
    if num not in l2:
        l3.append(num)

print("l1:", l1)
print("l2:", l2)
print("l3 (numbers in l1 that are not in l2):", l3)
