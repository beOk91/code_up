num1,num2=map(int,input().split())
gcd=1
lcm=1
for i in range(min(num1,num2),0,-1):
    if num1%i==0 and num2%i==0:
        gcd=i
        break
lcm=num1/gcd * gcd * num2/gcd
print("{}\n{}".format(gcd,int(lcm)))
"""



"""