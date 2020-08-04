num1=input()
num2=num1[::-1]
result=int(num1)+int(num2)
result2=str(result)
result3=result2[::-1]
if result2==result3:
    print("YES")
else:
    print("NO")