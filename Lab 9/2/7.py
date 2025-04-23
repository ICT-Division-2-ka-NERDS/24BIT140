def average(lst):
	if len(lst)==0:
		return 0
	return (lst[0] + average(lst[1:])) / len(lst)

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
	x = int(input("Enter number: "))
	lst.append(x)

print("Average of the numbers:", average(lst))
