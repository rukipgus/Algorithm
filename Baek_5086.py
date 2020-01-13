import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 0 and a[1] == 0:
        exit()
    if a[1]%a[0] == 0:
        print("factor")
    elif a[0]%a[1] == 0:
        print("multiple")
    else:
        print("neither")