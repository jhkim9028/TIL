# 1037

cnt = int(input())
A = list(map(int, input().split()))

ans = sorted(A)[0] * sorted(A)[-1]
print(ans)