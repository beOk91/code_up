def f(num):
    if num==1:
        return str(1)
    elif num%2==1:
        return f(num*3+1)+"\n"+str(num)
    else:
        return f(num//2)+"\n"+str(num)
num=int(input())
print(f(num))