a,b,c=map(int,input().strip().split())
if a>(b-c):
    print("do not advertise")
elif a<(b-c):
    print("advertise")
else:
    print("does not matter")