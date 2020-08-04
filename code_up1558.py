def f(num):
    val=""
    for i in range(len(num)-1,-1,-1):
        val+=num[i]
    return val
print(f(input()))