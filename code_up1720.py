num=int(input())
arr=[]
for i in range(num):
    a,b,c,d=map(int,input().strip().split())
    if min(a,b,c)!=d:
        arr.append([i+1,min(a,b,c)])
if len(arr)==0:
    print(-1)
else:
    print(arr[0][0],arr[0][1])
