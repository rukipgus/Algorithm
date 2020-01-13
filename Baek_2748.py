n = int(input())
a = 0
b = 1

for i in range(n):
    s = a
    a = b
    b = s+a

print(a)