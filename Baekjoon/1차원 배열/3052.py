import sys
num = []
ans = 0
for i in range(10):
    a = int(sys.stdin.readline().strip())
    if a%42 not in num:
        num.append(a%42)
        ans += 1
print(ans)

