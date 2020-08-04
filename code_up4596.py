arr=[[0 for i in range(9)] for i in range(9)]
for i in range(9):
    arr[i]=list(map(int,input().split()))
width,height=0,0
max=arr[width][height]
for i in range(9):
    for j in range(9):
        if max<arr[i][j]:
            max=arr[i][j]
            width=i+1
            height=j+1
print(max)
print(width,height)