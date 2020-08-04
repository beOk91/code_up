lotto_num=list(map(int,input().strip().split()))
bonus=lotto_num[6]
lotto_num.pop()
my_lotto=list(map(int,input().strip().split()))
cnt=0
for element in my_lotto:
    if element in lotto_num:
        cnt+=1

if cnt==6:
    print(1)
elif cnt==5:
    if bonus in my_lotto:
        print(2)
    else:
        print(3)
elif cnt==4:
    print(4)
elif cnt==3:
    print(5)
else:
    print(0)