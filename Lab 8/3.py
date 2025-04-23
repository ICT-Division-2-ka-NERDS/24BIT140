s=set()
for i in range(5):
    name=input("Enter a name:")
    s.add(name)
print(s)

modi=input("Enter the name you want to modify:")
s.remove(modi)
new=input("Enter the name you want to replace it with:")
s.add(new)

name1=input("Enter the first name to delete:")
name2=input("Enter the second name to delete:")
s.remove(name1)
s.remove(name2)

print(s)