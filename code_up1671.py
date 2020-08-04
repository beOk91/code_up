a,b=map(int,input().strip().split())
if a==0 and b==1:
    print("win")
elif a==1 and b==2:
    print("win")
elif a==2 and b==0:
    print("win")
elif a==b:
    print("tie")
else:
    print("lose")