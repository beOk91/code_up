n,g=map(int,input().strip().split())
n_list=list(map(int,input().strip().split()))
for i in range(0,n,g):
    val=-1000
    for j in range(i,i+g):
        if j<n:
            val=max(n_list[j],val)
    print(val,end=" ")