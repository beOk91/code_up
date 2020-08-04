arr=[[0]*4 for i in range(4)]
for i in range(3):
    arr[i][0],arr[i][1],arr[i][2]=map(int,input().split())

for i in range(3):
    arr[i][3]=arr[i][0]+arr[i][1]+arr[i][2]

for i in range(4):
    arr[3][i]=arr[0][i]+arr[1][i]+arr[2][i]

for i in range(4):
    for j in range(4):
        print(arr[i][j],end=" ")
    print()