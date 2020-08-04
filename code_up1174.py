hour,minute=map(int,input().split())
timeSum=hour*60+minute-30
print((timeSum//60+24)%24,timeSum%60)