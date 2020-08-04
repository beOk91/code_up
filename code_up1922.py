def f(num):
    if num==1:
        return [1]
    elif num%2==1:
        return f(num*3+1)+[num]
    else:
        return f(num//2)+[num]

num=int(input())
print(len(f(num)))