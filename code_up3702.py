r,c=map(int,input().strip().split())
arr=[[0]*c for i in range(r)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i==0 or j==0:
            arr[i][j]=1

for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        arr[i][j]=arr[i][j-1]+arr[i-1][j]

print(arr[r-1][c-1]%100000000)

