num=int(input())
arr=[[0]* i for i in range(1,num+1)]

for i in range(num):
    arr[i][0]=int(input())

for i in range(1,num):
    for j in range(1,i+1):
        arr[i][j]=arr[i][j-1]-arr[i-1][j-1]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()