def f(num,k):
    if k==0:
        return int(num[0])
    else:
        return f(num,k-1)+int(num[k])
num=input()
print(f(num,len(num)-1))
