k,n=map(int,input().strip().split())
arr=[[0]*k for i in range(k)]
for i in range(k):
    arr[i]=list(map(int,input().strip().split()))
cnt=0
for i in range(k):
    for j in range(k):
        if arr[i][j]!=-1:
            arr[i][j]+=n
        if arr[i][j]>=0 and arr[i][j]<=5:
            cnt+=1
if cnt==0:
    print(0)
else:
    print(cnt)