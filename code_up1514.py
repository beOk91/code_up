arr=[[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0] ]

for i in range(3):
    a,b=map(int,input().split())
    arr[a-1][b-1]=2

for i in range(7):
    for j in range(7):
        print(arr[i][j],end=" ")
    print()