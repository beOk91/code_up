num=int(input())
day=num//(3600 * 24) 
num%=(3600 * 24)
hour=num//3600
num%=3600
minute=num//60
num%=60
print(day,hour,minute,num)