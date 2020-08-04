n=int(input())
number,numberRange=0,sum(i for i in range(n+1))
arr=[[0]*n for i in range(n)]
x,y,flag,number=0,n-1,1,0
while number!=numberRange:
    if x>=n:
        flag=0
        x-=1
        y+=2
    elif y>=n:    
        flag=1
        x+=2
        y-=1
    
    number+=1
    arr[y][x]=number

    if flag==1:
        x+=1
        y-=1
    elif flag==0:
        x-=1
        y+=1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()