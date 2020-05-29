# Uses python3

n=int(input())
d={}
def f(n) :
    if (n<=1):
        return n
    else:
        if n in d:
            res=d[n]
        else:
            res=(f(n-1)+f(n-2))
            d[n]=res
        return res


print(f(n))