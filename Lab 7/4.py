st=input("Enter a string:")
di={}
for i in st:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
print(di)