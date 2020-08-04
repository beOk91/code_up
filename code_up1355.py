num=int(input())
for i in range(num,-1,-1):
    for j in range(num-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()