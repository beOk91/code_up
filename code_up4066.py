n,m=map(int,input().strip().split())
cnt,sets=0,0
while True:
    cnt= sets*(m+1)
    if cnt==n:
        cnt==cnt*n
        break
    elif cnt>n:
        cnt=(sets-1)*m+(sets-1)
        break
    sets+=1
    
print(cnt)