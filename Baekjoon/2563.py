import sys
input = sys.stdin.readline

n = int(input())

matrix = [[0 for _ in range(101)] for _ in range(101)]
        

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            matrix[i][j] = 1

ans = 0
for m in matrix:
    ans += m.count(1)

print(ans)
