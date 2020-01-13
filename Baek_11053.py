n = int(input())
a = list(map(int, input().split()))
b = [1 for i in range(n)]
count = 0

for i in range(n):
    for j in range(0,i):
        if a[i] > a[j]:
            if count < b[j]:
                count = b[j]
    b[i] += count
    count = 0

print(max(b))