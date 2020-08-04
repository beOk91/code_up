num1,num2=input().split()
sum=float(num1)
while True:
    if sum<=float(num2):
        print("%.2f" %sum)
        sum+=0.01
    else:
        break