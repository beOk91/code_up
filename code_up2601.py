arr=[0]*41
arr[1],arr[2]=1,1

num=int(input())
for i in range(3,num+1):
    arr[i]=arr[i-1]+arr[i-2]

print(arr[num])