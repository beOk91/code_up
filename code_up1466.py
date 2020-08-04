n,m=input().split()
num_list=[[0 for i in range(int(m))] for j in range(int(n))]
cnt=1
for i in range(int(m)-1,-1,-1):
    for j in range(int(n)-1,-1,-1):
        num_list[j][i]=cnt
        cnt+=1

for i in range(int(n)):
    for j in range(int(m)):
        print(num_list[i][j],end=" ")
    print()