def convert(st):
    words=st.split()
    unique_words=sorted(set(words))
    return ' '.join(unique_words)

st="apple banana apple orange banana cherry"
print(convert(st))
