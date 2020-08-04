num=int(input())
number=1
arr=[[0 for i in range(num)] for i in range(num)]
for i in range(num):
    for j in range(num):
        arr[i][j]=number
        number+=1
for i in range(num):
    for j in range(num):
        print(arr[i][j],end=" ")
    print()
