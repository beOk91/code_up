import sys
arr=[0]*100000000
n,d=map(int,sys.stdin.readline().strip().split())
for num in range(n):
    arr[sum(int(i) for i in str(num))]+=1
print(arr[d]% 1000000007)