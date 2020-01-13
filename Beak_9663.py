n = int(input())

def cq(a):
    global count

    if len(a) == n:
        count += 1
        return 0

    b = list(range(n))

    for i in range(len(a)):
        if a[i] in b:
            b.remove(a[i])

        c = len(a)-i

        if a[i]+c in b:
            b.remove(a[i]+c)
        if a[i]-c in b:
            b.remove(a[i]-c)

    if b == []:
        return
    else:
        for i in b:
            a.append(i)
            cq(a)
            a.pop()

count = 0

for i in range(n):
    cq([i])

print(count)