num=input()
sum1=0
for element in num:
    sum1+=int(element)
if sum1%7==4:
    print("suspect")
else:
    print("citizen")