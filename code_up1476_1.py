n,m=map(int,input().strip().split())
arr=[[0]*m for i in range(n)]    
number,x,y,start_x,start_y=0,0,0,0,0
while number!=n*m:
    if y==n:
        start_y-=1
        y=start_y
        start_x+=1
        x=start_x

    number+=1
    arr[y][x]=number
    x+=1
    y-=1

    if y<0 or x==m:
        start_y+=1
        y=start_y
        x=start_x    


for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()