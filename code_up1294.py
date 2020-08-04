code_list=["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
alpha_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
text=input()
for i in range(len(text)):
    if text[i] >='a' and text[i]<='z':
        print(alpha_list[code_list.index(text[i])],end="")
    else:
        print(" ",end="")