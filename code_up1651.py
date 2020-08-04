w,h,n=map(int,input().strip().split())
arr=[]
for i in range(n):
    arr.append(input())

for i in range(n):
    for _ in range(h):
        for j in range(len(arr[i])):
            for _ in range(w):
                print(arr[i][j],end="")
        print()