n=int(input())
dictionary_studentInfo={}
dictinonary_gender={}
sum1=0
for i in range(n):
    info=input().strip().split(",")
    dictionary_studentInfo[info[0]]=info[3:]
    dictinonary_gender[info[0]]=info[1]
name=input()
for friend in dictionary_studentInfo[name]:
    if dictinonary_gender[friend]=="M":
        sum1+=1
print(sum1)
print(len(dictionary_studentInfo[name])-sum1)