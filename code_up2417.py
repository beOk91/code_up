n=int(input())
dictinonary_cnt={}
for i in range(n):
    info=input().strip().split(",")
    registered_friend=info[3:]
    for name in registered_friend:
        dictinonary_cnt[name]= 0 if dictinonary_cnt.get(name)==None else dictinonary_cnt[name]+1
friend_cnt=0
friend_rank=[]
for element in dictinonary_cnt:
    if dictinonary_cnt[element]>friend_cnt:
        friend_cnt=dictinonary_cnt[element]
        friend_rank.clear()
        friend_rank.append(element)
    elif dictinonary_cnt[element]==friend_cnt:
        friend_rank.append(element)
friend_rank.sort()
for element in friend_rank:
    print(element)