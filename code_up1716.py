month,day=map(int,input().strip().split())
october_30=5*30 + 5*31
for i in range (1,month):
    if i%2==0:
        october_30-=30
    else:
        october_30-=31
print(october_30-day)