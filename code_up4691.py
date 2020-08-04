import math
num=int(input())
money=[]
for i in range(num):
    num_list=list(map(int,input().split()))
    dice_list=[]
    dice_dict={}
    for element in num_list:
        if element not in dice_list:
            dice_list.append(element)
            dice_dict[element]=1
        else:
            dice_dict[element]+=1        
    if max(dice_dict.values())==4:
        money.append(50000+dice_list[0]*5000)
    elif max(dice_dict.values())==3:   
        