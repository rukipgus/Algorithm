a = list(map(int, input().split()))
b = max(a)
c = min(a)

while True:
    d = c
    c = b%c
    b = d
    if c == 0:
        print(b)
        print(a[0]*a[1]//b)
        exit()

