def f(num,cnt):
    if cnt-1!=num:
        print(cnt)
        f(num,cnt+1)
        
num=int(input())
f(num,1)