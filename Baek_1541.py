a = list(input())
b = ""
c = ""
d = 0
e = []
f = 0

for i in a:
    if i == "+" or i == "-":
        b += i
        e.append(int(c))
        c = ""
    else:
        c += i

e.append(int(c))
f = e[0]
del e[0]

for i in range(len(e)):
    if i == 0:
        c = b.find("-")
        if c == -1:
            f += sum(e)
        else:
            f += sum(e[:c])

    if b[i] == "-":
        c = b[i+1:].find("-")
        if c != -1:
            f -= sum(e[i:i+c+1])
        else:
            f -= sum(e[i:])
            break

print(f)