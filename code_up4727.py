import sys,math
gcd_val,lcm_val=map(int,sys.stdin.readline().strip().split())
ab_1,minVal=lcm_val//gcd_val,gcd_val+lcm_val
a,b=0,0
for i in range(1,ab_1//2+1):
    if ab_1%i==0 and math.gcd(i,ab_1//i)==1:
        if minVal>i+ab_1//i:
            minVal=i+ab_1//i
            a,b=i,ab_1//i
a,b=1 if gcd_val==lcm_val else a,1 if gcd_val==lcm_val else b
print(a*gcd_val,b*gcd_val)

"""
import sys,math
a,b=map(int,sys.stdin.readline().strip().split())
c=b//a
i=int(math.sqrt(c))
while i>0:
    if c%i==0 and math.gcd(i,c//i)==1:
        break
    i-=1
print(i*a,b//i)
"""

"""
6 180
->30 36

16 32
->16 32

35 771260
->
980 27545
내답: 3955 6825
"""