num1,num2=map(int,input().split())
number,z=1,0
arr=[[i for i in range(num2)] for i in range(num1)]
for i in range(num2-1,-1,-1):
    if z%2==0:
        for j in range(num1-1,-1,-1):
            arr[j][i]=number
            number+=1
    else:
        for j in range(num1):
            arr[j][i]=number
            number+=1
    z+=1

for i in range(num1):
    for j in range(num2):
        print(arr[i][j],end=" ")
    print()