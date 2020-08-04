num=int(input())
arr,idx=[],0
for i in range(num):
    arr.append(int(input()))
arr2=[0]*num
arr2[0]=arr[0]
arr2[1]=arr[0]+arr[1]
arr2[2]=max(arr[0]+arr[2],arr[1]+arr[2])

for i in range(3,num):
    arr2[i]=max(arr2[i-3]+arr[i-1]+arr[i],arr2[i-2]+arr[i])
print(arr2[num-1])