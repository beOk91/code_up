n,m=map(int,input().strip().split())
arr=[[0]*m for i in range(n)]  
number=1
for val in range(n+m-1):
    for i in range(n-1,-1,-1):
        for j in range(m):
            if i+j==val:
                arr[i][j]=number
                number+=1
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()

arr2=[[0]*m for i in range(n)]    
number2,x,y,start_x,start_y=0,0,0,0,0
while number2!=n*m:
    if y==n:
        start_y-=1
        y=start_y
        start_x+=1
        x=start_x

    number2+=1
    arr2[y][x]=number2
    print(y,x)
    x+=1
    y-=1

    if y<0 or x==m:
        start_y+=1
        y=start_y
        x=start_x    


for i in range(n):
    for j in range(m):
        print(arr2[i][j],end=" ")
    print()
"""
0,0   ->0
1,0 0,1 ->1
2,0 1,1 0,2 ->2
"""
"""
2,1 1,2 0,3 ->3
2,2 1,3 ->4
2,3 ->5
"""