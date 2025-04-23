def reverse_list(lst):
	if len(lst)<=1:
		return lst
	return [lst[-1]]+reverse_list(lst[:-1])

n=int(input("Enter number of elements: "))
lst=[]
for i in range(n):
	num=int(input("Enter number: "))
	lst.append(num)
print("Original list:",lst)
print("Reversed list:",reverse_list(lst))
