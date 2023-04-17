import sys
input = sys.stdin.readline

N = int(input())
ans = {}

numbers = list(map(int, input().split()))

num = sorted(list(set(numbers)))

ans = {num[i]:i for i in range(len(num))}

for i in numbers:
    print(ans[i], end=' ')