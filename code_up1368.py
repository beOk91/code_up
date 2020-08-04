num1,num2,direction=input().split(" ")
if direction=="L":
    for i in range(int(num1)):
        for j in range(i):
            print(" ",end="")
        for j in range(int(num2)):
            print("*",end="")
        print()
else:
    for i in range(int(num1)):
        for j in range(int(num1)-i-1):
            print(" ",end="")
        for j in range(int(num2)):
            print("*",end="")
        print()