text=list(map(str,input().strip().split(";")))
for i in range(len(text)):
    text[i]=text[i].strip()
    if text[i][len(text[i])-1]==",":
        temp=text[i][:len(text[i])-1]
        text[i]=temp
        print(len(text[i]))
    else:
        text[i]=list(map(int,text[i].split(",")))

for i in range(len(text)):
    for j in range(len(text[i])):
        print(text[i][j],end=" ")
    print()
    
    """
    2,5408    ,   -5786   ,  -8201 ;  
    7748,10471,16878,-11862;
    -10704,
    2,5408    ,   -5786   ,  -8201 ;  7748,10471,16878,-11862;-10704,
    """