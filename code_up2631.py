import sys
n,k=map(int,sys.stdin.readline().strip().split())
n_list=list(map(int,sys.stdin.readline().strip().split()))
cnt=0
for i in range(n):
    if n_list[i]>k:
        break
    temp=0
    for j in range(i,n):
        temp+=n_list[j]
        if temp==k:
            cnt+=1
            break
        elif temp>k:
            break
print(cnt)