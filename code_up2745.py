a,b,c=map(int,input().strip().split())
day=0
while a>=0:
    a-=b
    if a<=0:
        day+=1
        break
    a+=c
    day+=1
print(day)

"""
5 3 2

a=2
day=1
a=4

a=1
day=2
a=3
"""