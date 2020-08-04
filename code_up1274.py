def sosu(num):
    cnt=0
    for i in range(1,num+1):
        if num%i==0:
            cnt+=1
        if cnt>2:
            return False
    if cnt==2:
        return True
    return False
num=int(input())
if sosu(num):
    print("prime")
else:
    print("not prime")
def prime(number):
    if number!=1: