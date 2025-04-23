faculty=['Ravi','Anil','Priya','Kiran','Venkatesh']
filtered_names=list(filter(lambda name:len(name)>8,faculty))
for i in filtered_names:
	print(i)

