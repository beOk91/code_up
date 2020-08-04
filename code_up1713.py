a,b=map(int,input().strip().split())
sum=0
for i in range(a,b+1):
    if i%12!=0:
        if i%3==0:
            sum+=i
        elif i%4==0:
            sum-=i
print(sum)