voca=input()
cnt=0
for i in range(len(voca)):
    voca2=""
    if i <len(voca)-3:
        for j in range(i,i+4):
            voca2+=voca[j]
    if voca2=="love":
        cnt+=1
print(cnt)