fin=open("8_in.txt","r")
fout=open("8_out.txt","w")
for line in fin:
    words=line.split()
    modified_words=[]
    for word in words:
        if word.lower() in ['a','the','an']:
            modified_words.append(' ')
        else:
            modified_words.append(word)
    fout.write(' '.join(modified_words)+'\n')
fin.close()
fout.close()
print("The new file has been created successfully!")



