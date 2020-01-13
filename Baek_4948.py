import sys

a = []
b = 1

while b != 0:
    b = int(sys.stdin.readline())
    if b == 0:
        break
    a.append(b)

c = [False, False] + [True for i in range(2*max(a))]
d = len(c)

for i in range(2,d):
    for j in range(2*i,d,i):
        if c[j] == True:
            c[j] = False


for i in a:
    e = 0
    for j in range(i+1,2*i+1):
        if c[j] == True:
            e+=1
    print(e)