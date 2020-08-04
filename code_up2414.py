n=int(input())
dictionary_age={}
for i in range(n):
    info=input().strip().split(",")
    dictionary_age[info[0]]=int(info[2])
name=input()
print(dictionary_age[name])