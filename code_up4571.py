import math
num1=int(input())
num2=int(input())
sum=0
min=0
for i in range(num2,num1-1,-1):
    if math.sqrt(i)%1==0:
        sum+=i
        min=int(i)
if sum==0:
    print(-1)
else:
    print("{}\n{}".format(sum,min))