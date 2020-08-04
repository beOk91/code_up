sum=0
num=int(input())
arr=[[0 for i in range(num)] for i in range(num)]
number=1
for i in range(num):
    for j in range(num):
        arr[i][j]=number
        if i==0 or i ==num-1 or j==0 or j==num-1:
            sum+=number
        number+=1
print(sum)