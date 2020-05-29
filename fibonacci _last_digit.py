# Uses python3
n=int(input())
d={}
def f(n) :
    if (n<=1):
        return n
    else:
        a = 0
        b = 1
        for i in range(2,n+1):
            if n in d:
                b=d[i]
            else:
                a,b=b %10,(a+b )%10
                d[i]= b
        return b
print(f(n))