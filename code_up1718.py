text=input()
whereH=text.index("H")
if text[whereH-1]=="C":
    c_val=1
else:
    c_val=int(text[1:whereH])
if len(text)-1==whereH:
    h_val=1
else:
    h_val=int(text[whereH+1:])
print(c_val*12+h_val)