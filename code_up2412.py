n=int(input())
sum_Age=0
for i in range(n):
    info=input().strip().split(",")
    sum_Age+=int(info[2])
print("%.2f" %(round(sum_Age/n,2)))
