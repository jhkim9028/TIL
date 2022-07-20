import sys

sys.stdin = open("2043_input.txt", "r")

p, k = map(int, input().split())
ans = 0
if p >= k:
    ans += (p - k + 1)
else:
    ans += (k - p + 1)
print(ans)