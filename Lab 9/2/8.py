def string_length(s):
	if s=="":
		return 0
	else:
		return 1+string_length(s[1:])
	
s=input("Enter a string:")
print("Length of the string:",string_length(s))
