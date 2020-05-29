# Uses python3
n,m=map(int,input().split())
d = {}
def f(n,m):
    if (n <= 1):
         return n
    else:
         a = 0
         b = 1
         for i in range(2, n + 1):
                 a, b = b % int(m), (a + b) % int(m)
         return b
print(f(n,m))