def sosu(num):
    if num==1:
        return False
    for i in range(num-1,1,-1):
        if num%i==0:
            return False
    return True
m=int(input())
n=int(input())
sum=0
minValue=0

for i in range(n,m-1,-1):
    if sosu(i):
        sum+=i
        minValue=i

if minValue==0:
    print(-1)
else:
    print(sum)
    print(minValue)