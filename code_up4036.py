n=int(input())
m=int(input())
a,b=0,0
for i in range(2,n):
    if i-(n-i)==m:
        a=i
        b=n-i
        break
print(a)
print(b)
