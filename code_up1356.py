num=int(input())
for i in range(num):
    if i==0 or i==num-1:
        for j in range(num):
            print("*",end="")
    else:
        print("*",end="")
        for j in range(num-2):
            print(" ",end="")
        print("*",end="")
    print()