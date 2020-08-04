r,g,b=input().split(" ")
cnt=0
for i in range(int(r)):
    for j in range(int(g)):
        for k in range(int(b)):
            print("{} {} {}".format(i,j,k))
            cnt+=1
print(cnt)