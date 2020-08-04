def f(num_list):
    result=num_list
    while True:
        result2=0
        for i in range(len(result)):
            result2+=int(result[i])
        result=str(result2)
        if len(result)==1:
            break
    return result
num_list=input().strip()
print(f(num_list))