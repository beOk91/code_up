n,m=map(int,input().strip().split())
arr=[[0]*m for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()