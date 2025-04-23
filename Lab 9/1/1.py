def count_case(st):
    di={"upper": 0, "lower": 0}
    for i in st:
        if i.isupper():
            di["upper"]+=1
        elif i.islower():
            di["lower"]+=1
    return di

txt="Hello World"
print(count_case(txt))
