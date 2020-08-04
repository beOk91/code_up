num=int(input())
arr=[]
arr.append(1)
arr.append(2)
for i in range(2,num):
    arr.append(arr[i-1]+arr[i-2])
print(arr[num-1]%100000007)