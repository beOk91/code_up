m,s1,s2=map(int,input().strip().split())
add_score=0
for i in range(m,90,5):
    add_score+=1
new_s1=s1+add_score
if new_s1>s2:
    print("win")
elif new_s1<s2:
    print("lose")
else:
    print("same")
