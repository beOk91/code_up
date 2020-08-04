val=1
for i in range(3):
    a,b=map(int,input().split())
    if val<a*b:
        val=a*b
print(val)