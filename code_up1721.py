import math
a,b=map(int,input().strip().split())
c,d=map(int,input().strip().split())

result=round(math.sqrt((c-a)**2+(d-b)**2),2)
print("%.2f" %result)