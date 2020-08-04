def gcd(a,b):
    if a>=b:
        r=a%b
        if r==0:
            return b
        else:
            return gcd(r,b)
    else:
        return gcd(b,a)

def lcm(a,b):
    c=gcd(a,b)
    return int(a/c)*int(b/c)*c

num1,num2=map(int,input().strip().split())
print(lcm(num1,num2))
