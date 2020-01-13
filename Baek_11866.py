n, k = map(int, input().split())

a = [n-i for i in range(n)]
b = []

while True:
    if len(a) == 0:
        print("<", end = "")
        for i in range(n-1):
            print(b[i], end = ", ")
        print(b[-1], end = "")
        print(">")
        break

    for i in range(1, k):
        c = a.pop()
        a.insert(0, c)
    
    b.append(a.pop())