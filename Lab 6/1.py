boys_count=0
girls_count=0
names=[("Arjun",),("Rahul",),"Priya","Sita",("Vikram",),"Anjali"]

for ele in names:
    if isinstance(ele, tuple):
        boys_count+=1
    else:
        girls_count+=1

print(boys_count)
print(girls_count)
