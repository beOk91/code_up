import math
def f(n,r):
    if n<r:
        return 0
    else:
        return int(math.factorial(n)/math.factorial(n-r)/math.factorial(r))

n,r=map(int,input().strip().split())
print(f(n,r))