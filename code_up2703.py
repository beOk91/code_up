n=int(input())
n_list=list(map(int,input().strip().split()))
val1=0
val2=0
for i in range(n-1):
    if n_list[i]<n_list[i+1]:
        val1+=1
    elif n_list[i]>n_list[i+1]:
        val2+=1
print(val1,val2)