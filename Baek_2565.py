import sys

n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
    b.append(1)

a.sort(key = lambda x: x[0])

for i in range(n):
    c = 0
    for j in range(0,i):
        if a[j][1] < a[i][1]:
            if c < b[j]:
                c = b[j]
    b[i] +=c

print(n-(max(b)))