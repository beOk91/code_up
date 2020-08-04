def f(num):
    if num>=90:
        return 'A'
    elif num>=80:
        return 'B'
    elif num>=70:
        return 'C'
    elif num>=60:
        return 'D'
    else:
        return 'F'
num=int(input())
print(f(num))