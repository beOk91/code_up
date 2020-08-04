n=int(input())
sum_m=0
sum_f=0
for i in range(n):
    info=input().strip().split(",")
    if info[1]=="M":
        sum_m+=1
    else:
        sum_f+=1
print(sum_m)
print(sum_f)