def ispangram(s):
    alphaset=set('abcdefghijklmnopqrstuvwxyz')
    stset=set(s.lower())
    if alphaset<=stset:
        return "It is pangram"
    else:
        return "It is not pangram"

st1="The quick brown fox jumps over the lazy dog"
st2="Crazy Fredrick bought many very exquisite opal jewels"

print(ispangram(st1))  
print(ispangram(st2))  
