n=int(input())
dictionary_studentInfo={}
for i in range(n):
    info=input().strip().split(",")
    dictionary_studentInfo[info[0]]=info[3:]
name=input()
for friend in dictionary_studentInfo[name]:
    print(friend)