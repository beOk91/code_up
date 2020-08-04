text1,text2=input().strip().split()
for i in range(ord(text1),ord(text2)+1):
    print(chr(i),end=" ")