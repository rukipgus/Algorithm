a = list(input())
b = list(input())
c = [0 for i in range(len(b))]

for i in range(len(a)):
    d = 0
    e = [0 for j in range(len(b))]

    for j in range(len(b)):
        if a[i] == b[j]:
            e[j] = d+1
        if d < c[j]:
            d = c[j]
    for j in range(len(b)):
        if e[j] != 0:
            c[j] = e[j]

print(max(c))