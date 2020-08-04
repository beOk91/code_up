num=int(input())
text=input()
for i in range(1,len(text)+1):
    print(chr((ord(text[i-1])-(3*i+num)-ord('A'))%26+ord('A') ),end="")


"""
3
FXAB
"""