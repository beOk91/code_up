def f(num):
    if num==0:
        return 0
    elif num==1:
        return str(num%2)
    else:
        return f(num//2)+str(num%2)
num=int(input())
print(f(num))
