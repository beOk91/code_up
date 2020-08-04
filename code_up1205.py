num1,num2=map(int,input().strip().split())
myNum=max(num1+num2,num1-num2,num2-num1,num1*num2,num1/num2,num2/num1,num1**num2,num2**num1)
print("%.6f" %myNum)