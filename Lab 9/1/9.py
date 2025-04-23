def count_alpha_digits(st):
    di={"alphabets":0,"digits":0}
    for char in st:
        if char.isalpha():
            di["alphabets"]+=1
        elif char.isdigit():
            di["digits"]+=1
    return di

st="Hello 123 World 456"
print(count_alpha_digits(st))
