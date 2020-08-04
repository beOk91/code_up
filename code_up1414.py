text=input()
text=text.upper()
sum1,sum2=0,0
for i in range(len(text)):
    if text[i]=="C":
        sum1+=1
for i in range(len(text)-1):
    if text[i:i+2]=="CC":
        sum2+=1
print(sum1)
print(sum2)