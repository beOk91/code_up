num=int(input())
bad_program=[]
for i in range(num):
    programName=input()
    if len(programName)<=3 or "tap" in programName or "xocure" in programName:
        bad_program.append(programName)
for element in bad_program:
    print(element)
if len(bad_program)<=3:
    print("safe")
elif len(bad_program)<=6:
    print("warning")
else:
    print("danger")