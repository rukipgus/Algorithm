import sys

a = int(input())

b = [[0]+list(map(int, sys.stdin.readline().split())) for i in range(a)]

for i in range(a-1):
    for j in range(i+1, a):
        if b[i][1] < b[j][1] and b[i][2] < b[j][2]:
            b[i][0]+=1

        if b[i][1] > b[j][1] and b[i][2] > b[j][2]:
            b[j][0]+=1

for i in range(a):
    print(b[i][0]+1, end=" ")