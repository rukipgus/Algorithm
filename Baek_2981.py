import sys
import math

n = int(input())
a = []
b = []

a.append(int(sys.stdin.readline()))

for i in range(n-1):
    a.append(int(sys.stdin.readline()))

c = a[-1] - a[0]

for i in range(2, int(math.sqrt(c))+1):
    if c % i == 0:
        b.append(i)
        b.append(c//i)

b.append(c)
b = list(set(b))
b.sort()

print(b)

for i in b:
    d = a[0]%i
    for j in a:
        if j%i != d:
            break
        if j == a[-1]:
            print(i, end = " ")