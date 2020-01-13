import sys

n, k = map(int, input().split())
a = []
b = 0

for i in range(n):
    a.insert(0, int(sys.stdin.readline()))

for i in a:
    b += k//i
    if k//i != 0:
        k = k%i

print(b)