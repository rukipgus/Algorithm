import sys
max_val = [0]*2
a = [0]*9

for i in range(9):
    a[i] = int(sys.stdin.readline())
    if max_val[0] < a[i]:
        max_val[0] = a[i]
        max_val[1] = i

print("{}\n{}".format(max_val[0], max_val[1]+1))