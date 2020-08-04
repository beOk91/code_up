num1,num2=map(int,input().strip().split())
for z in range(num2):
    for i in range(num1):
        for j in range(i):
            print(" ",end="")
        print("*")
    for i in range(num1-1):
        for j in range(num1-i-2):
            print(" ",end="")        
        print("*")