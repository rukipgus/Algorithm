n = int(input())
a = [(n-i) for i in range(n)]
b = 1
while True:
    if n // b == 1:
        if n % b == 0:
            print(b)
            exit()
        else:
            print(2*(n % b))
            exit()
    b *= 2