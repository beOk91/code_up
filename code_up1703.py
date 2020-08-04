num=int(input())
hour=num//3600
num%=3600
minute=num//60
num%=60
print(hour,minute,num)