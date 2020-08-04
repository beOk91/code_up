num=input()
if len(num)==1:
    num="0"+num
new_num=int(num[1]+num[0])*2
if new_num>100:
    new_num%=100
if new_num<=50:
    print(new_num)
    print("GOOD")
else:
    print(new_num)
    print("OH MY GOD")

