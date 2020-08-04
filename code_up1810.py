text=list(input())
a,b=map(int,input().strip().split())
cnt=len(text)-b
for _ in range(cnt):
    text.pop(len(text)-1)
for _ in range(a-1):
    text.pop(0)
for element in text:
    print(element,end="")