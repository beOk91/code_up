n=int(input())
arr=[0]*20
arr[0],arr[1]=2,3
for i in range(2,n):
    arr[i]=arr[i-1]+arr[i-2]
print(arr[n-1])