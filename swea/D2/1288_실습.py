import sys

sys.stdin = open("1288_input.txt", "r")

T = int(input())

# set, list 중 하나 사용
for i in range(1,T+1):
    N = int(input())
    N1 = N
    num = set()
    while True:
        for n in str(N):
            num.add(n)
        # print(n, num)
        if len(num) == 10:
            break
        N += N1
    print(f'#{i} {N}')