first,last=input().split(" ")
for i in range(int(first),int(last)+1):
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j))