def f(n,k):
    if n==1:
        return 1
    elif n==-1:
        if k%2==1:
            return -1
        else:
            return 1
    if k==0:
        return 1
    else:
        return n*f(n,k-1)

n,k=map(int,input().strip().split())
print(f(n,k))