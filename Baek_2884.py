a,b = map(int, input().split())

if b < 45:
    print((a-1)%24 ,(b-45)%60)
else:
    print(a, b-45)