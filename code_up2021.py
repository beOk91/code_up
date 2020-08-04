num=int(input())
arr=[[0]*2 for i in range(num)]

for i in range(num):
    arr.append(int(input()))
print(max(arr)-min(arr))