num_list=list(map(int,input().strip().split()))
oddMax=-1
evenMax=-1
for element in num_list:
    if element%2==0 and element>evenMax:
        evenMax=element
    elif element%2!=0 and element>oddMax:
        oddMax=element
if oddMax==-1:
    print(evenMax)
elif evenMax==-1:
    print(oddMax)
else:
    print(oddMax,evenMax)