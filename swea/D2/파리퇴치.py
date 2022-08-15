import sys
sys.stdin = open('파리퇴치_input.txt')

T = int(input())
sum_ = []
for t in range(T):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_ = 0
            for x in range(m):
                for y in range(m):
                    sum_ += area[i+x][j+y]
            if sum_ > result:
                result = sum_
    print(result)
    # print(f'#{t+1} {max(sum_)}')
