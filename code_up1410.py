text,cnt1,cnt2=input(),0,0
for i in range(len(text)):
    if text[i]=="(":
        cnt1+=1
    elif text[i]==")":
        cnt2+=1
print(cnt1,cnt2)