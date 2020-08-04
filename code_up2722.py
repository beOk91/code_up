def f(n):
    if n==1:
        return 5
    elif n==2:
        return 12
    else:
        return int(n*5+2*n+ (n-2)*(n-1)*3/2)
num=int(input())
print(f(num))



     