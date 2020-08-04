def f(num_list):
    num1,num2=map(int,num_list.split())
    sum=0
    arr=[0 for i in range(num2+1)]

    for i in range(num2):
        chk=0
        for j in range(len(str(i))):
            chk+=int(str(i)[j])
        chk+=int(str(i))
        if chk <=num2:
            arr[chk]=1

    for i in range(num1,num2+1):
        if arr[i]!=1:
            sum+=i
    return sum

num_list=input().strip()
print(f(num_list))