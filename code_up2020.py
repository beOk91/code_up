text=input().strip()
aroma_dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
idx=0
result=0
while idx!=len(text):
    if idx==len(text)-2:
        result+=int(text[idx])*aroma_dictionary[text[idx+1]]
    elif aroma_dictionary[text[idx+1]]>=aroma_dictionary[text[idx+3]]:
        result+=int(text[idx])*aroma_dictionary[text[idx+1]]
    else:
        result-=int(text[idx])*aroma_dictionary[text[idx+1]]
    idx+=2
print(result)