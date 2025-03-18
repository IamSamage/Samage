case = int(input())

for i in range(1, case + 1):
    a, b = map(int, input().split())
    print('Case #%d: %d + %d ='%(i, a, b), (a + b))