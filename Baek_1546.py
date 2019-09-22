import sys

a = int(input())
avg = 0.0

b = list(map(int, sys.stdin.readline().split()))

m = max(b)

for i in range(a):
    avg += b[i]/m*100

print(avg/a)