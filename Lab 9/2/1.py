def prime_factors(n,divisor=2):
    if n==1:
        return
    if n%divisor==0:
        print(divisor,end=' ')
        prime_factors(n//divisor,divisor)
    else:
        prime_factors(n,divisor+1)

num=int(input("Enter a number:"))
print("Prime factors of",num,"are:",end=' ')
prime_factors(num)

