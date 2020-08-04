n,k=map(int,input().strip().split())
n_list=list(map(int,input().strip().split()))
for i in range(n):
    if n_list[i]>=k:
        print(i+1)
        break
    if i==n-1 and n_list[n-1]<k:
        print(n+1)