arr=[[0] * 9 for i in range(9)]
for i in range(9):
    arr[i]=list(map(int,input().strip().split()))
r,c=map(int,input().strip().split())

if arr[r-1][c-1]==1:
    print(-1)
else:
    min_cnt=0
    for i in range(r-2,r+1):
        for j in range(c-2,c+1):
            if i>=0 and j>=0 and j<=8 and i<=8 and arr[i][j]==1:
                min_cnt+=1
    print(min_cnt)
