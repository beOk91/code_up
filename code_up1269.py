a,b,c,n=map(int,input().strip().split())
arr=[0]*n
arr[0]=a
for i in range(1,n):
    arr[i]=arr[i-1]*b+c
print(arr[n-1])