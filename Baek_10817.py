a, b, c = map(int, input().split())

if a > b:
    j = b
    b = a
    a = j
if b > c:
    j = c
    c = b
    b = j
if a > b:
    j = b
    b = a
    a = j

print(b)