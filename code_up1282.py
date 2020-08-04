import math
num=int(input())
for i in range(1,num):
    if math.sqrt(num-i)%1==0:
        print(i,int(math.sqrt(num-i)))
        break