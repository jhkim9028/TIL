# 델타 탐색
# 규칙 1
# N = 5일 때, 첫줄은 아래로 5개, 그 다음 오른쪽, 위로 4개씩, 그 다음 왼쪽, 아래 3개씩 ...
# 5, 4, 4, 3, 3, 2, 2, 1, 1
# 규칙 2
# 모든 달팽이는 N * 2 - 1 번 방향 전환

from pprint import pprint

# N x N
N = int(input())

# 좌표를 출력할 숫자
k = int(input())

# 델타탐색 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


snail = [[0 for _ in range(N)] for _ in range(N)]

n = N ** 2

# 방향때문에
d = -1

# -1, 0으로 시작해야 0,0
x = -1
y = 0

m = N

ans = []

for i in range(N * 2 - 1):
    # 이렇게 해야 d 값이 0,1,2,3,0,1,2,3... -> 방향
    d = (d + 1) % 4
    for j in range(m):
        x += dx[d]
        y += dy[d]
        
        snail[x][y] = n
        
        n -= 1
        
        # 입력받은 숫자에 도달하면
        if n == k:
            ans.extend([x+1, y+1])
    if not d or not d % 2:
        m -= 1

        
        
print(snail)