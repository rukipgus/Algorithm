a = int(input())
b = 0

for i in range(a):
    if sum(map(int, list(str(i))))+i == a:
        b = i
        break

print(b)