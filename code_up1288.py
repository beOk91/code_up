def nCr(n,r):
    if n==r:
        return 1
    return int(factorial(n)/factorial(n-r)/factorial(r))
def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

n,r=map(int,input().split())
print(nCr(n,r))