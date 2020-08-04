num1,num2=input().split(" ")
if int(num1)%5==0:
    print(int((90-int(num1))/5)+int(num2))
else:
    print(int((90-int(num1))/5)+int(num2)+1)