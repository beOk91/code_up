def f(num):
    print(num)
    if num==1:
        return
    elif num%2==1:
        num=3*num+1
        f(num)
    else:
        num=int(num/2)
        f(num)
num=int(input())
f(num)