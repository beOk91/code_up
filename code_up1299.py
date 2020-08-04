a,b,c=map(int,input().strip().split())
flag=False
for i in range(-1000,1001):
    for j in range(-1000,1001):
        if a*i+b*j==c:
            print(i,j)
            flag=True
            break
    if flag:
        break    
if not flag:
    print("Not Exist")