def f(num):
    if num==1:
        return f2(1)
    else:
        return f(num-1)+"\n"+f2(num)
def f2(num):
    if num==1:
        return str(num)
    else:
        return f2(num-1)+" "+str(num)
num=int(input())
print(f(num))