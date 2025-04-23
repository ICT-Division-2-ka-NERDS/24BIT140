def generate(end):
    li=[]
    for x in range(1,end+1):
        li.append((x,x**2,x**3))
    return li

end_value=5
print(generate(end_value))
