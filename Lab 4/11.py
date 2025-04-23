def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def sin_x(x,N):
    result=0
    for n in range(N):
        term=(((-1)**n)*(x**(2*n+1)))/factorial(2*n+1)
        result+=term
    return result

x=float(input("Enter the value of x (in radians):"))
N=int(input("Enter the number of terms (N):"))
result=sin_x(x,N)
print("sin(x) =",result)

