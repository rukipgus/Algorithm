import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

for i in range(a[0]):
    if b[i]<a[1]:
        print(b[i],end=" ")