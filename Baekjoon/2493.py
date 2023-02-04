# # 역순으로 해서 while을 써서 i+1번째가 i번쨰보다 크거나 같으면 ans에 추가
# # i+1 번째가 i번째보다 작으면 반복
# # 완전탐색
# # 시간초과

# # 탑 개수
# N = int(input())
# # 탑
# top = list(map(int, input().split()))
# # 탑역순
# r_top = top[::-1]
# # 처음은 0고정
# ans = [0]

# # 첫번째는 0으로 고정이기 때문에
# for i in range(len(top)-1):
#     a = i
#     while True:
#         if r_top[a+1] >= r_top[i]:
#             ans.insert(1,N-a-1)
#             break
#         if r_top[i] > r_top[a+1]:
#             a += 1
#         if a + 1 == N and r_top[i] > r_top[a]:
#             ans.insert(1,0)
#             break

# print(*ans)

# 순서대로 돌린다.
# 만약 스택이 비어있으면 ans에 0, 스택에 인덱스와 값을 넣는다.
# 스택에 마지막 값과 비교해서 비교값이 더 크면 스택의 마지막값을 제거 계속 비교해서 더 크거나 같은 값이 나오면 비교하던 값을 스택에 쌓고 ans에 인덱스 추가

# 탑 개수
N = int(input())
# 탑
top = list(map(int, input().split()))

stack = []
ans = []


for k, v in enumerate(top):
    if not len(stack):
        stack.append([k+1,v])
        ans.append(0)
        continue
    while True:
        if stack[-1][-1] >= v:
            ans.append(stack[-1][0])
            stack.append([k+1,v])
            break
        if v > stack[-1][-1]:
            stack.pop()
            if not len(stack):
                stack.append([k+1,v])
                ans.append(0)
                break
print(*ans)