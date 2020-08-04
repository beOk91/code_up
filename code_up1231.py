cal=input()
if "+" in cal:
    num1,num2=map(int,cal.split("+"))
    print(num1+num2)
elif "-" in cal:
    num1,num2=map(int,cal.split("-"))
    print(num1-num2)
elif "*" in cal:
    num1,num2=map(int,cal.split("*"))
    print(num1*num2)
else:
    num1,num2=map(int,cal.split("/"))
    print("%.2f" %(num1/num2))