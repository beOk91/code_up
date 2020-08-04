def f(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input())
if num==1 or num==2 or num==3:
    print("wrong number")
for i in range(2,num):
    if num%i==0 and f(i) and f(num//i):
        print(i,num//i)
        break
    elif i==num-1 and num%i!=0:
        print("wrong number")
    