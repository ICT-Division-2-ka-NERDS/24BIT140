st=input("Enter a string:")
alphacount,digicount=0,0
for i in st:
    if i.isalpha():
        alphacount+=1
    elif i.isdigit():
        digicount+=1
print("Number of alphabets in the string:",alphacount)
print("Number of digits in the string:",digicount)