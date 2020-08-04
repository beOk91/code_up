num=int(input())
if num <=500:
    num=num*70/100
elif num <=1500:
    num=350+(num-500)*40/100
elif num <=4500:
    num=750+(num-1500)*15/100
elif num <=10000:
    num=1200+(num-4500)*5/100
else:
    num=1475+(num-10000)*2/100
print(int(num))