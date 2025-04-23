name={"Arjun","amit","Bhanu","bala","Anjali","bina","Anand"}
a=set()
b=set()
for i in name:
    if i[0]=='A' or i[0]=='a':
        a.add(i)
    elif i[0]=='B' or i[0]=='b':
        b.add(i)
print("Names starting with 'A' or 'a':",a)
print("Names starting with 'B' or 'b':",b)