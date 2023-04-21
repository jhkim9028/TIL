import sys
input = sys.stdin.readline

n = int(input())


ans = 1
for i in range(2,n+1):
    if i*i <= n:
        ans += 1
    elif i*i > n:
        break
print(ans)