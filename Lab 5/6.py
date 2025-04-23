n=int(input("Enter the number of records:"))
farli=[]
for i in range(n):
    far=float(input("Enter farenheit temperature:"))
    farli.append(far)

celli=[]
for i in farli:
    celli.append((5/9)*(i-32))

print("Farenheit:",farli)
print("Celcius",celli)