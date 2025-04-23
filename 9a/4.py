lst=['madam','Python','malayalam',12321]
palindrome=list(filter(lambda item:type(item)==str and item==item[::-1],lst))
print("Palindrome strings:",palindrome)

