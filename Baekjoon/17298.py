# 스택에 큰 수를 넣는게 아니라
# 작은 수를 넣고 큰 수가 나오면 한번에 와르르

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

stack = [0]
ans = [-1] * N


for i in range(1,N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)


print(*ans)




