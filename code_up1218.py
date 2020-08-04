import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
num_list=list(map(int,input().strip().split()))
num_list.sort()
if num_list[2]<(num_list[0]+num_list[1]):
    if num_list[0]== num_list[1] and num_list[1]==num_list[2]:
        print("정삼각형")
    elif num_list[0]== num_list[1] or num_list[1]==num_list[2]:
        print("이등변삼각형")
    elif num_list[2]**2==(num_list[0]**2+num_list[1]**2):
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형아님")