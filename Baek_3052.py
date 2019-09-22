import sys

a = [0]*10
t = 0

for i in range(10):
    a[i] = int(sys.stdin.readline())%42

a = list(set(a))
print(len(a))