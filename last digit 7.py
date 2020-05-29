# Uses python3
m,n=map(int,input().split())
d={}
def f(m,n) :
    if (n<=1):
        return n
    if m<1:
        b=1
        a=0
        sum = b
        for i in range(m+2,n+1):
            if i in d:
                sum = d[i]
            else:
                a, b = b, a +b
                sum += b
                d[i]=sum

    elif m==1:
        b=1
        a=0
        sum = b
        for i in range(m+1,n+1):
            if i in d:
                sum = d[i]
            else:
                a, b = b, a + b
                sum += b
                d[i] = sum
    else:
        a=0
        b=1
        for  _ in range(m-1):
            a,b=b,a+b

        sum = b
        for i in range(m+1,n+1):
            if i in d:
                sum = d[i]
            else:
                a, b = b, a + b
                sum += b
                d[i] = sum
    return sum %10
print(f(m,n))