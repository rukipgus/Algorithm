import sys

a = int(input())
b = list(map(int, sys.stdin.readline().split()))

print("%d %d" %(min(b), max(b)))