num=int(input())
arr=[]
for i in range(num):
    idx,amt=map(int,input().split())
    arr.append((idx,amt))
arr.sort(key=lambda x:x[0])
for i in range(num):
    print(arr[i][0],arr[i][1])