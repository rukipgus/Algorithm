import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
    if i == 0:
        continue

    for j in range(len(a[i])):
        if j == 0:
            a[i][j] = a[i-1][j]+a[i][j]
        elif j == i:
            a[i][j] = a[i-1][j-1]+a[i][j]
        else:
            a[i][j] = a[i][j] + max(a[i-1][j], a[i-1][j-1])

print(max(a[n-1]))