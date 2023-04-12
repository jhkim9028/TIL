import sys
input = sys.stdin.readline
N = int(input())

number = []

for _ in range(N):
    a, b = map(int, input().split())
    number.append([a,b])
number.sort(key=lambda x:(x[0],x[1]))
for n in number:
    print(n[0],n[1])
#     number.append([a,b])

# number = sorted(number)
# for i in range(N):
#     print(*number[i])






# num = []
# for _ in range(N):
#     a,b = map(int,input().split())
#     num.append([a,b])

# stack = []
# arr = []
# for i in range(N):
#     if not stack:
#         stack.append(num[i])
#         continue
#     if num[i][0] == stack[-1][0] and num[i][1] < stack[-1][1]:
#         while True:
#             if stack[-1][1] <= num[i][1]:
#                 stack.append(num[i])
#                 while arr:
#                     stack.append(arr.pop())
#                 break
#             arr.append(stack.pop())
#     elif num[i][0] < stack[-1][0]:
#         while True:
#             if not stack or stack[-1][0] < num[i][0] and stack[-1][1] < num[i][1]:
#                 stack.append(num[i])
#                 while arr:
#                     stack.append(arr.pop())
#                 break
#             arr.append(stack.pop())
#     else:
#         stack.append(num[i])

# for j in range(len(stack)):
#     print(*stack[j])