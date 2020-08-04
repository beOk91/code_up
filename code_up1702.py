a,b,c=map(int,input().strip().split())
if b%2!=0:
    print(str(a)+str(b)+str(c))
else:
    for i in range(2):
        print(str(a)+str(b)+str(c))