fin1=open("6_1_in.txt","r")
fin2=open("6_2_in.txt","r")
fout=open("6_out.txt","w")
st1=fin1.readlines()
st2=fin2.readlines()

maxst=max(len(st1),len(st2))
for i in range(maxst):
    if i<len(st1):
        fout.write(st1[i])

    if i<len(st2):
        fout.write(st2[i])

fin1.close()
fin2.close()
fout.close()
print("New file created successfully")


