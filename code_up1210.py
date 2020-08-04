calory_dictionary={
    "1":400,
    "2":340,
    "3":170,
    "4":100,
    "5":70
}
num1,num2=input().split()
sum=calory_dictionary[num1]+calory_dictionary[num2]
if sum>500:
    print("angry")
else:
    print("no angry")