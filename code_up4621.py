n,k=map(int,input().split())
arr=[0 for i in range(n)]
cnt=0
for i in range(1,n+1):
    if n%i ==0:
        arr[cnt]=i
        cnt+=1
if arr[k]==0:
    print(0)
else:
    print(arr[k-1])