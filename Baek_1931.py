import sys

n = int(input())
a = []
b = []
c = 1

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort(key = lambda a: (a[1], a[0]))
b.append(a[0])

while True:
    d = 0
    for i in range(c,n):
        if a[i][0] >= b[-1][1]:
            b.append(a[i])
            c = i+1
            d = 1
            break
    if d == 0:
        break

print(len(b))