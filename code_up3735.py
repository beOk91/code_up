num=int(input())
num_list=list(map(int,input().strip().split()))
arr=[0]*num
for i in range(num):
    myNum=arr[i]
    cnt=0
    for j in range(i+1,num):
        if myNum<arr[j]:
            