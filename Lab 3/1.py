st=input("Enter a string")
count=0
for i in st:
    if i in "aeiouAEIOU":
        count+=1
print("Number of vowels in the string are:",count)