k,n=map(int,input().strip().split())
k_list=list(map(int,input().strip().split()))
for i in range(k,n):
    sum=0
    for j in range(i-1,i-k-1,-1):
        sum+=k_list[j]
    k_list.append(sum)

print(k_list[n-1]%100007)
"""
2 3
7 7 14 
1,
"""