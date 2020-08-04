num1,num2=map(int,input().strip().split())
for i in range(num2):
    for j in range(num1):
        if (i==0 or i==num2-1) and (j==0 or j==num1-1):
            print("+",end="")
        elif i==0 or i==num2-1:
            print("-",end="")
        elif (i!=0 or i!=num2-1):
            if j==0 or j==num1-1:
                print("|",end="")
            else:
                print(" ",end="")
    print()