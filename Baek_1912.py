n = int(input())
a = list(map(int, input().split()))
b = [a[0]]

for i in range(len(a)-1):
    b.append(max(b[i]+a[i+1], a[i+1]))

print(max(b))
