f=open("q2.csv","r")
data={}
rows=f.readlines()
for r in rows[1:]:           
    record=r.strip().split(',')
    rollno=int(record[0])
    name=record[1]
    sub1=int(record[2])
    sub2=int(record[3])
    sub3=int(record[4])
    total=sub1+sub2+sub3
    data[rollno]={"Name":name,"Sub_1":sub1,"Sub_2":sub2,"Sub_3":sub3,"Total":total}
print(data)
f.close()