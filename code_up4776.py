easy="JKLABCDEFGHI" ##12
period="7890123456" ##10
year=int(input())
year%=60
print(easy[year%len(easy)-1],end="")
print(period[year%len(period)-1],end="")
