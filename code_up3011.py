num=int(input())
arr=list(map(int,input().strip().split()))
cnt=0
for i in range(num):
    change_flag=False
    for j in range(num-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            change_flag=True
    if change_flag:
        cnt+=1
print(cnt)