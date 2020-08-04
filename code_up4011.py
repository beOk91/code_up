id1,id2=input().split("-")
year,month,day,gender=0,0,0,""
if id2[0] in ["3","4"]:
    year=2000+int(id1[:2])
else:
    year=1900+int(id1[:2])
month=int(id1[2:4])
day=int(id1[4:7])
gender ="M" if id2[0] in ["1","3"] else "F"
print(str("%.4d/%.2d/%.2d " %(year,month,day))+gender ,end="")