sum=0
money=0
for i in range(5):
    start,end=map(float,input().split())
    day=end-start-1
    if day>4:
        day=4
    elif day<0:
        day=0
    sum+=day
if sum>=15:
    money=sum*10000*0.95
elif sum<=5:
    money=sum*10000*1.05
else:
    money=sum*10000
print(int(money))