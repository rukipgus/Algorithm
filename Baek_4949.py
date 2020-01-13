import sys

while True:
    a = sys.stdin.readline()
    b = []
    c = 0

    if a == ".\n":
        break

    for i in a:
        if i == "(":
            b.append("(")
        elif i == ")":
            if len(b) == 0:
                c = 1
                break
            if b[-1] == "(":
                b.pop()
            else:
                c = 1
                break
        elif i == "[": 
            b.append("[")
        elif i == "]":
            if len(b) == 0:
                c = 1
                break
            if b[-1] == "[":
                b.pop()
            else:
                c = 1
                break

    if c == 0 and len(b) == 0:
        print("yes")
    else:
        print("no")