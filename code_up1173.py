hour,minute=input().split()
if int(minute) <30:
    minute=(60+(int(minute)-30))
    hour=int(hour)-1
else:
    minute=int(minute)-30
print(hour,minute)