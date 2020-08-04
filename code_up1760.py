text=input()
text2=input()
for i in range(len(text2)):
    if text2[i] in text:
        print(text.index(text2[i]),end="")
    else:
        print(text2[i],end="")