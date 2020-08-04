year,day=map(int,input().strip().split())
day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or year%400==0:
    if day==2:
        day_list[day-1]+=1
print(day_list[day-1])
