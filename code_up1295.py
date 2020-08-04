sentence=input()
sentence2=""
for i in range(len(sentence)):
    if sentence[i]>='a' and sentence[i]<='z':
        sentence2+=sentence[i].upper()
    else:
        sentence2+=sentence[i].lower()
print(sentence2)