a,b,c=map(int,input().strip().split())
y=0
for i in range(1,c):
    if (c-(b*i))%a==0:
        y=i
        break
if y==0:
    print("Not Exist")
else:
    print((c-(b*y))//a,y)