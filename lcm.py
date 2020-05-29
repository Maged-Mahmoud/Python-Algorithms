# Uses python3
a,b=map(int,input().split())


def gcd(a, b):
    while b != 0:
        a, b = b,int(a % b)
    return int(a)


def lcm(a, b):
    return (a * b // gcd(a, b))
print(lcm(a,b))
