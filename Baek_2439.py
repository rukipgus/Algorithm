import sys
a = int(sys.stdin.readline())

for i in range(a):
    print(" "*(a-i-1) + "*"*(i+1))