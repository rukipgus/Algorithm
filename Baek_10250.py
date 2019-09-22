import sys

a = int(input())

for i in range(a):
    b,c,d = map(int, sys.stdin.readline().split())
    if d%b == 0:
        print("{}{:>02d}".format(b, (d//b)))
    else:
        print("{}{:>02d}".format((d%b), (d//b)+1))