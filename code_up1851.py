def f(num):
    if num==1:
        return "*"
    else:
        return "*"+f(num-1)
num=int(input())
print(f(num))