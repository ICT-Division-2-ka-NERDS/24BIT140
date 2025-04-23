def create_list(li1,li2):
    result=[]
    for i in li1:
        if i in li2 and i not in result:
            result.append(i)
    return result

li1=[1,2,3,4,5]
li2=[4,5,6,7]
print(create_list(li1,li2))
