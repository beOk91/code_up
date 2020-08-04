def f(num):
    if num==1:
        return 1
    else:
        return num*f(num-1)
n,k=map(int,input().strip().split())
space=k+1
space2=n-k*2+1
if space2<0:
    print(0)
else:
    print(int(f(space+space2-1)/f(space+space2-1-space2)/f(space2)))