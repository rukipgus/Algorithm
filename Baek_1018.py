import sys

a, b = map(int, sys.stdin.readline().split())
c = []
d = [["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"], ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]]
answer = 64


for i in range(a):
    c += [sys.stdin.readline()]

for i in range(a-7):
    for j in range(b-7):
        answer1 = 0
        answer2 = 0

        for k in range(8):
            for v in range(8):
                if d[0][k][v] != c[i+k][j+v]:
                    answer1 +=1
                if d[1][k][v] != c[i+k][j+v]:
                    answer2 +=1
        answer = min(answer1, answer2, answer)

print(answer)