a,b=map(int,input().strip().split())
c,d=map(int,input().strip().split())
flag=False
a,b=min(a,b),max(a,b)
c,d=min(c,d),max(c,d)   

if (a>c and b<d) or (a<c and b>d):
    flag=False
else:
    for j in range(c,d+1):
        if a<=j and j<=b:
            flag=True
            break
if flag:
    print("cross")
else:
    print("not cross")