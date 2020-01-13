n = int(input())

a = list(map(int, input().split()))
b = [1 for i in range(n)]
c = [1 for i in range(n)]
count1 = 0
count2 = 0

for i in range(n):
    for j in range(0,i):
        if a[j] < a[i]:
            if count1 < b[j]:
                count1 = b[j]
        if a[n-i-1] > a[n-j-1]:
            if count2 < c[n-j-1]:
                count2 = c[n-j-1]
    b[i] += count1
    c[n-i-1] += count2
    count1 = 0
    count2 = 0

for i in range(n):
    b[i] += c[i]

print(max(b)-1)