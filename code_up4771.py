text=input()
sum=10
for i in range(1,len(text)):
    if text[i-1]!=text[i]:
        sum+=10
    else:
        sum+=5
print(sum)
