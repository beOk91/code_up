num1,num2=input().split()
num_list=[[0 for i in range(int(num2))] for j in range(int(num1))]
cnt=1
for i in range(int(num2)-1,-1,-1):
    for j in range(int(num1)):
        num_list[j][i]=cnt
        cnt+=1

for i in range(int(num1)):
    for j in range(int(num2)):
        print(num_list[i][j],end=" ")
    print()