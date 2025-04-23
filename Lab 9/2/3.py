def count_vowels(s):
	if len(s)==0:
		return 0
	
	if s[0] in "AEIOUaeiou":
		return 1+count_vowels(s[1:])
	else:
		return count_vowels(s[1:])
	
s=input("Enter a string:")
print("Number of vowels:",count_vowels(s))
