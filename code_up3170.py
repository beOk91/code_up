n,m=map(int,input().split())
arr={}
for i in range(n):
    s,k=input().split()
    arr[s]=arr.get(s,0)+int(k)

for i in range(m):
    q=input()
    print(arr.get(q,0))

"""
for i in range(m):
    if q in arr:
        print(arr.get(q,0))
    else:
        print(0)