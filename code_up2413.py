n=int(input())
sum_friend=0
for i in range(n):
    info=input().strip().split(",")
    sum_friend+=len(info)-3
print("%.2f" %(round(sum_friend/n,2)))
