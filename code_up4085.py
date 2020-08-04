m,n,x,y=map(int,input().strip().split())
arr=[[0]*m for i in range(n)]
arr2=[[0]*(m-x+1) for i in range(n-y+1)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))

for i in range(n-y+1):
    for j in range(m-x+1):
        for k in range(i,i+y):
            for l in range(j,j+x):
                arr2[i][j]+=arr[k][l]
maxVal=arr2[0][0]
for i in range(n-y+1):
    for j in range(m-x+1):
        maxVal=max(maxVal,arr2[i][j])
print(maxVal)