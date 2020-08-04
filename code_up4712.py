num=int(input())
arr=[0]*3
for i in range(num):
    a,b,c=map(int,input().strip().split())
    arr[0]+=a
    arr[1]+=b
    arr[2]+=c
print(arr)
print(arr.index(max(arr)),max(arr))
