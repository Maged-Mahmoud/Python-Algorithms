# Uses python3
n=int(input())
def f(n) :
    if (n<=1):
        return n
    a=0
    b=1
    sum=1
    for _ in range(n-1):
        a,b=b,a+b
        sum+=b
    return sum % 10
f(n)
print(f(n))