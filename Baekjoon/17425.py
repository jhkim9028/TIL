# 1은 (n // 1) * 1 번
# 2는 (n // 2) * 2 번...

# pypy3

# 테스트 케이스
import sys

input = sys.stdin.readline

a = 10 ** 6

# fx
yak = [1] * (a + 1)

# gx
ans = [0] * (a + 1)

# 메모리제이션
# fx 채우기
for i in range(2, a + 1):
    for j in range(i, a + 1, i):
        yak[j] += i

# gx 채우기
for i in range(1, a + 1):
    ans[i] = ans[i-1] + yak[i]

for t in range(int(input())):
    N = int(input())
    print(ans[N])
    

