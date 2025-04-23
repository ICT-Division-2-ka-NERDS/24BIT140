def sanitize(lst):
	if len(lst)==0:
		return []
	
	if lst[0]<0:
		return [0]+sanitize(lst[1:])
	else:
		return [lst[0]]+sanitize(lst[1:])
	
n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
	num=int(input("Enter number:"))
	lst.append(num)
print("Sanitized list:",sanitize(lst))
