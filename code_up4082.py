amt,alchohol_degree,weight,gender=map(float,input().strip().split())
hour,minute=map(int,input().strip().split())
c=(amt*alchohol_degree/100*0.7984)/(weight*(0.7 if gender==1 else 0.6))/10
ct=round(c-(0.015*((hour*60+minute-30)/60)),3)
if ct<0:
    ct=0
if ct>=0.08:
    print("%.3f cancel" %ct)
elif ct>=0.03:
    print("%.3f stop" %ct)
else:
    print("%.3f pass" %ct)
"""
- 총 11개 중 7번째 테스트 케이스 - 
점수 = 55 / 100

입력:
500.7 21.3 59.4 1
24 10
"""