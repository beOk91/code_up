n,m=map(int,input().strip().split())
arr=[[0]*m for i in range(n)]       
number=1
for val in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i+j==val:
                arr[i][j]=number
                number+=1
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
