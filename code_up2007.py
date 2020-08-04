import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n=int(input())
n_list=list(map(int,input().strip().split()))
flag1,flag2=True,True
for i in range(n-1):
    if n_list[i]<n_list[i+1]:
        flag2=False
    elif n_list[i]>n_list[i+1]:
        flag1=False
if flag1:
    print("오름차순")
elif flag2:
    print("내림차순")
else:
    print("섞임")    
