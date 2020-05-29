# Uses python3
x1=int(input())
x=list(map(int,input().split()))
a=max(x)
x.remove(a)
b=max(x)
result=a*b
print(result)
