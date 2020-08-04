import sys
sys.setrecursionlimit(10000)
arr=[0]*10001
arr[1]=1
def nCr(n,r):
    ##return int(int(factorial(n)/factorial(n-r))/factorial(r))%100000007
def factorial(n):
    if arr[n]!=0:
        return arr[n]
    else:
        arr[n]=(n*factorial(n-1))
        return arr[n]

n,r=map(int,input().split())
print(nCr(n,r))
