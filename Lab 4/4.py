def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def armstrong(num):
    digits = str(num)
    return num == sum(int(d)**len(digits) for d in digits)

def palindrome(num):
    s = str(num)
    return s == s[::-1]

def automorphic(num):
    return str(num**2).endswith(str(num))

num=int(input("Enter a number:"))

print("Prime:",prime(num))
print("Perfect:",perfect(num))
print("Armstrong:",armstrong(num))
print("Palindrome:",palindrome(num))
print("Automorphic:",automorphic(num))
