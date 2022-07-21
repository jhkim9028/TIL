import sys

sys.stdin = open("1976_input.txt", "r")

# 1시 16분 3시 48분 = 시는 더한다. 만약 더한 값이 12가 넘으면 -12
# 분은 더한다. 만약 더한 값이 59를 넘으면 시에 1더하고 -60한다.

T = int(input())


for i in range(1, T+1):
    a, b, c, d= map(int, input().split())
    time = a + c
    minute = b + d
    if time > 12:
        time = time - 12
    if minute > 59:
        time = time + 1
        minute = minute - 60
    print(f'#{i} {time} {minute}')