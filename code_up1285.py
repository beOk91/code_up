text=input()
idx=0
result=0
while True:
    if text[idx]=="=":
        break
    elif text[idx] not in ["+","-","*","/","="]:
        temp=""
        while text[idx] not in ["+","-","*","/","="]:
            temp+=text[idx]
            idx+=1
        result+=int(temp)
    elif text[idx] in ["+","-"]:
        temp=""
        temp+=text[idx]
        idx+=1
        while text[idx] not in ["+","-","*","/","="]:
            temp+=text[idx]
            idx+=1
        result+=int(temp)
    elif text[idx] =="*":
        temp=""
        idx+=1
        while text[idx] not in ["+","-","*","/","="]:
            temp+=text[idx]
            idx+=1
        result*=int(temp)
    elif text[idx] =="/":
        temp=""
        idx+=1
        while text[idx] not in ["+","-","*","/","="]:
            temp+=text[idx]
            idx+=1
        result=result//int(temp)      

print(int(result))