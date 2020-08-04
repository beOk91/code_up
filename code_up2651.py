n,k=map(int,input().split())
cnt=1
for i in range(n,n-k,-1):
    cnt*=i
for i in range(k,0,-1):
    cnt/=i
print(int(cnt))