import sys
arr=[0]*10000000
num1=int(sys.stdin.readline().strip())
num1_list=list(map(int,sys.stdin.readline().strip().split()))
for element in num1_list:
    arr[element]=1
num2=int(sys.stdin.readline().strip())
num2_list=list(map(int,sys.stdin.readline().strip().split()))
ans = list(map(lambda n : n in num1_list, num2_list))
for _ in range(0, len):
    print("%d"%ans[_], end=" ")