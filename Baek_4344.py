import sys

a = int(input())

for i in range(a):
    b, *c = map(int, sys.stdin.readline().split())
    aveg = sum(c)/b
    d = 0.0
    for k in range(b):
        if c[k] > aveg:
            d +=1
    print("{:0.3f}%".format((d/b)*100))