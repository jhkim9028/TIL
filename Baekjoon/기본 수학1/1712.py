# A : 고정비용
# B : 가변 비용
# C : 판매 가격
import sys
A, B , C = map(int, sys.stdin.readline().split())

# 고정 비용 + 가변 비용 * 판매수(ans) > C * 판매수(ans)
com = 0

while True:
    if B >= C:
        print(-1)
        break
    else:
        com = A // (C - B) + 1
        print(com)
        break