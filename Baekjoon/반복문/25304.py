X = int(input())

N = int(input())
ans = 0
for n in range(N):
    a, b = map(int, input().split())
    ans = ans + (a * b)

if ans == X:
    print('Yes')
else:
    print('No')