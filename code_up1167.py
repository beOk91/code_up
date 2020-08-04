val_list=input().split(" ")
val_list2=[]
for i in range(len(val_list)):
    val_list2.append(int(val_list[i]))
val_list2.remove(max(val_list2))
val_list2.remove(min(val_list2))
for i in range(len(val_list2)):
    print(val_list2[i])
