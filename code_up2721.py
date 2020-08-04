num1=input()
num2=input()
num3=input()
if num1[len(num1)-1]==num2[0]:
    if num2[len(num2)-1]==num3[0]:
        if num3[len(num3)-1]==num1[0]:
            print("good")
        else:
            print("bad")
    else:
        print("bad")
else:
    print("bad")