num=int(input())
for i in range(num):
    for j in range(num):
        if i==0 or j==0 or i==num-1 or j==num-1 or j==num-i-1 or i==j or i==int(num/2) or j==int(num/2):
            print("*",end="")
        else:
            print(" ",end="")
    print()