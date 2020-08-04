text=input()
arr=text.strip().split()
num_dictionary={
    "0":"zero", 
    "1":"one", 
    "2":"two", 
    "3":"three", 
    "4":"four", 
    "5":"five", 
    "6":"six", 
    "7":"seven", 
    "8":"eight", 
    "9":"nine"
}
for i in range(len(arr)):
    if arr[i]=="i" or arr[i] in ("i?","i!","i."):
        arr[i]=arr[i].upper()
    elif i==0:
        arr[i]=arr[i][0].upper()+(arr[i].lower())[1:]
    elif arr[i][0:] in "0123456789":
        arr[i]=num_dictionary[arr[i]]
    else:
        arr[i]=arr[i].lower()
for element in arr:
    print(element,end=" ")