def f(num):
    if num<0:
        num*=-1
    return num

num=float(input())
print("%.10g" %f(num))