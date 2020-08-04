money=int(input())
day=int(input())
num_list=list(map(int,input().strip().split()))
presentMoney=money
for element in num_list:
    presentMoney=presentMoney*(100+element)/100
presentMoney=round(presentMoney)-money
print(presentMoney)
if presentMoney>0:
    print("good")
elif presentMoney==0:
    print("same")
else:
    print("bad")