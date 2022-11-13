chess = [1,1,2,2,2,8]

x = input().split()

ans = []
for i in range(len(chess)):
    ans.append(chess[i] - int(x[i]))
print(*ans)