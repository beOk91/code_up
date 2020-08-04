import sys
def f(n,k):
    if k==0:
        return 1
    elif k%2==0:
        val=f(n,k//2)
        return (val*val)%1000000007
    else:
        return (n*f(n,k-1))%1000000007
n,k=map(int,sys.stdin.readline().strip().split())
print(f(n,k))

