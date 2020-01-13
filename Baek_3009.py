import sys
answer=[]
a = []

for i in range(3):
    a.append(list(map(int, sys.stdin.readline().split())))

if a[0][0] == a[1][0]:
    answer.append(a[2][0])
elif a[0][0] == a[2][0]:
    answer.append(a[1][0])
else:
    answer.append(a[0][0])

if a[0][1] == a[1][1]:
    answer.append(a[2][1])
elif a[0][1] == a[2][1]:
    answer.append(a[1][1])
else:
    answer.append(a[0][1])
    
print(answer[0], answer[1])