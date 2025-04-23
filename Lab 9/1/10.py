def frequency(st):
    words=st.split()
    freq={}
    for i in words:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return dict(sorted(freq.items()))

st="apple banana apple orange banana apple"
print(frequency(st))
