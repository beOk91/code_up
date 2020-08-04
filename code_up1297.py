num=int(input())
maxValue=1
maxWidth=1
for i in range(1,num):
    if i*(num-i*2)>maxValue:
        maxValue=i*(num-i*2)
        maxWidth=i
print(maxWidth)