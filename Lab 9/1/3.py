def create_array(x,y,z,val):
    l1=[]
    for i in range(x):
        l2=[]
        for j in range(y):
            l3=[]
            for k in range(z):
                l3.append(val)
            l2.append(l3)
        l1.append(l2)
    return l1

arr=create_array(3,4,5,7)
print(arr)
