num=int(input())
arr=[]
for i in range(1,num+1):
    arr.append(i)
for i in range(num-1):
    num1=int(input())
    arr.remove(num1)
print(arr[0])