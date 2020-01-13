n = int(input())
a = list(map(int, input().split()))

def gcd(x,y):
    b = max(x,y)
    c = min(x,y)

    while True:
        d = c
        c = b%c
        b = d
        if c == 0:
            return b

for i in a[1:]:
    print("{}/{}".format((a[0]//gcd(a[0],i)), (i//gcd(a[0],i))))