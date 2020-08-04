num1,num2=input().split()
age=0
if num2[0] in ["3","4"]:
    age=2012-2000-int(num1[0:2])+1
    print(age,"M" if num2[0]=="3" else "F")
else:
    age=2012-1900-int(num1[0:2])+1
    print(age,"M" if num2[0]=="1" else "F")