a,b,c,d=map(int,input().strip().split())
if a/b > c/d:
    print(">")
elif a/b==c/d:
    print("=")
else:
    print("<")