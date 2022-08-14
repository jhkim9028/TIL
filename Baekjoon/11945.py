import sys
sys.stdin = open('11945_input.txt')
n, m = map(int, input().split())

bread = [input() for _ in range(n)]



for i in range(n):
    ans = ''
    for j in range(m)[::-1]:
        ans += bread[i][j]
    print(ans)