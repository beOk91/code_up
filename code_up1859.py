def f(num):
    if num==1:
        return "*"
    else:
        return f(num-1)+"\n"+"*"*num
num=int(input())
print(f(num))
