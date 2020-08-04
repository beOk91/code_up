def f(num):
    if num==1:
        return "1"
    else:
        return f(num-1)+" "+ str(num)
num=int(input())
print(f(num))