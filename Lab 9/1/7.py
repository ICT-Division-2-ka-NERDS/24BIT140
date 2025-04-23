def ispalindrome(s):
    s=s.replace(" ", "").lower()  
    if s==s[::-1]:
        return "It is palindrome"
    else:
        return "It is not palindrome"

print(ispalindrome("Racecar"))  
print(ispalindrome("Hello"))  
