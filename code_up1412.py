arr=[0]*26
text=input()
for i in range(len(text)):
    if text[i] >='a' and text[i]<='z':
        arr[ord(text[i])-97]+=1
for i in range(len(arr)):
    print("{}:{}".format(chr(i+97),arr[i]))