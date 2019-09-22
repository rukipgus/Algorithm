import sys

a = int(input())
b = [""]*a

for i in range(a):
    b[i] = sys.stdin.readline()

for i in range(a):
    score = 0
    hel = 0
    for k in range(len(b[i])):
        if b[i][k] == "O":
            hel += 1
            score += hel
        else:
            hel = 0
    print(score)