import collections

n, k = map(int, input().split())

a = collections.deque([])
b = 0
a.append(n)
a.append("!")
g = [True]*200001

while True:
    d = a.popleft()

    if d == "!":
        b += 1
        d = a.popleft()
        a.append("!")

    if d == k:
        break

    if d-1 == k or d+1 == k or 2*d == k:
        b += 1
        break

    if d-1 >= 0:
        if g[d-1] == True:
            a.append(d-1)
            g[d-1] = False

    if d+1 < 100001:
        if g[d+1] == True:
            a.append(d+1)
            g[d+1] = False

    if 2*d < 200001:
        if g[2*d] == True:
            a.append(2*d)
            g[2*d] = False

print(b)