import sys

T = int(sys.stdin.readline())

for t in range(T):
    ans = ''
    R, S = map(str, sys.stdin.readline().split())
    for s in S:
        ans += s*int(R)
    print(ans)