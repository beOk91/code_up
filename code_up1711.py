import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
x1,y1=map(int,input().strip().split())
x2,y2=map(int,input().strip().split())
x3,y3=map(int,input().strip().split())
if x3>=x1 and y3>=y1 and x3<=x2 and y3<=y2:
    print("충돌")
else:
    print("비충돌")