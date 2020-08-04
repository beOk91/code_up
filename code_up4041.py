num=input()
num2=""
num3=0
for i in range(len(num)-1,-1,-1):
    num2+=num[i]
    num3+=int(num[i])
print(int(num2))
print(num3)