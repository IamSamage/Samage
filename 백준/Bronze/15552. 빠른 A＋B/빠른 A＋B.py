import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(a+b)