import copy

a = int(input())
b = set(map(int, input().split()))
c = list(range(2,1001))
u = set(c)

for i in c:
    d = [j for j in c if j % i == 0]
    del d[0]
    k = set(d)
    u=u-k
u = u & b
x = list(u)
x.sort()
print(len(x))