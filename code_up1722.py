import math
num=int(input())
arr=[]
sum1=0
for i in range(num):
    arr.append(list(map(int,input().strip().split())))

for i in range(1,num):
    sum1+=math.sqrt((arr[i][0]-arr[i-1][0])**2+(arr[i][1]-arr[i-1][1])**2)
print("%.2f" %sum1)