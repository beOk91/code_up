k,n=map(int,input().strip().split())
cnt=0
while k>=n:
    coffee=int(k/n)
    cnt+=coffee
    k=k-(coffee*n)+coffee
print(cnt)