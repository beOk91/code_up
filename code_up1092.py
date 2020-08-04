p1,p2,p3=input().split(" ")
day=2
while day%int(p1)!=0 or day%int(p2)!=0 or day%int(p3)!=0:
    day+=1
print(day)