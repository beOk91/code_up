n= int(input())
arr= [0]*100001
arr[1]=1
arr[2]=2
arr[3]=4

for i in range(4,100001):
    arr[i]=(arr[i-3]+arr[i-2]+arr[i-1])%1000
print(arr[n])