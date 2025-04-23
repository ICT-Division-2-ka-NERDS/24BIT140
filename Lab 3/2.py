def uppercase():
    upst=''
    st=input("Enter a string:")
    for i in st:
        if 'z'>=i>='a':
            temp=ord(i)
            temp-=32
            c=chr(temp)
            upst+=c
        else:
            upst+=i
    print(upst)

def lowercase():
    lowst=''
    st=input("Enter a string:")
    for i in st:
        if 'Z'>=i>='A':
            temp=ord(i)
            temp+=32
            c=chr(temp)
            lowst+=c
        else:
            lowst+=i
    print(lowst)

def togglecase():
    newst=''
    st=input("Enter a string:")
    for i in st:
        if 'z'>=i>='a':
            temp=ord(i)
            temp-=32
            c=chr(temp)
            newst+=c
        elif 'Z'>=i>='A':
            temp=ord(i)
            temp+=32
            c=chr(temp)
            newst+=c
        else:
            newst+=i
    print(newst)

uppercase()
lowercase()
togglecase()
    
