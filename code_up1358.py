num=int(input())
for i in range(1,num+1,2):
    for j in range(int((num-i)/2)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()