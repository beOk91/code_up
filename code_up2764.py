name=input()
arr=["+","-"]
for i in range(len(name)*2+1):
    print(arr[i%2],end="")
print()
print("|"+"|".join(name)+"|")
for i in range(len(name)*2+1):
    print(arr[i%2],end="")