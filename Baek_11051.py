a = list(map(int, input().split()))
b = min(a[1], a[0]-a[1])
c = 1

for i in range(b):
    c *= (a[0]-i)
    c //= (i+1)

print(int(c)%10007)