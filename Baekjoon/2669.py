matrix = [[0] * 101 for _ in range(101)]

for _ in range(4):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            matrix[i][j] = 1
ans = 0
for k in range(len(matrix)):
    ans += matrix[k].count(1)

print(ans)