num=int(input())
for i in range(num):
    for j in range(num*2):
        if j== num-i-1 or j==num+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(num):
    for j in range(num*2):
        if i==j or j==num*2-i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


"""
0,4 0,5
1,3 1,6
2,2 2,7
3,1 3,8
4,0 4,9

0,0 0,9
1,1 1,8
2,2 2,7
3,3 3,6
4,4 4,5


"""