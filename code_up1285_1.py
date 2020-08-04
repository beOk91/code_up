text=input()
num_list=[]
operator_list=[]
temp=""
for i in range(len(text)):
    if text[i] in ["+","-","*","/","="]:
        num_list.append(int(temp))
        temp=""
        operator_list.append(text[i])
    else:
        temp+=text[i]

result=num_list[0]
idx=0
while idx!=len(operator_list)-1:
    if operator_list[idx]=="+":
        result+=num_list[idx+1]
        idx+=1    
    if operator_list[idx]=="-":
        result-=num_list[idx+1]
        idx+=1    
    if operator_list[idx]=="*":
        result*=num_list[idx+1]
        idx+=1
    elif operator_list[idx]=="/":
        result//=num_list[idx+1]
        idx+=1
    
print(int(result))