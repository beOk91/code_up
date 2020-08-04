num=int(input())
arr=[0]*15
arr[0],arr[1],arr[2]=1,2,4
for i in range(3,num):
    arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
print(arr[num-1])