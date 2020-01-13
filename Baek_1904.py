n = int(input())

a = 1
b = 1
for i in range(n):
    t = a%15746
    a = b%15746
    b = a+t

print(a)