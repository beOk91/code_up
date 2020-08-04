odd_min=100
odd_sum=0
for i in range(7):
    num=int(input())
    if num%2==1:
        odd_sum+=num
        if odd_min>num:
            odd_min=num
if odd_min==100:
    print(-1)
else:
    print(odd_sum)
    print(odd_min)