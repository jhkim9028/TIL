# import sys
# input = sys.stdin.readline

# n = int(input())

# num = [int(input()) for _ in range(n)]
# # 평균
# avg = sum(num) / n
# if sum(num) // n + 1 > avg >= sum(num) // n + 0.5:
#     avg = sum(num) // n + 1
# else:
#     avg = int(avg)
# print(avg)

# # 중앙값
# middle = sorted(num)
# print(middle[n//2])

# # 최빈값(여러개면 2번째로 작은 값)
# many = 0
# m = []
# for i in range(n):
#     a = num.count(num[i])
#     if a > many:
#         many = a
#         m.append(num[i])
# if len(m) == 1:
#     print(m[0])
    
# else:
#     m = sorted(m)
#     print(m[1])


# # 범위
# Min = min(num)
# Max = max(num)
# print(Max-Min)

import sys
input = sys.stdin.readline

n = int(input())

num = [int(input()) for _ in range(n)]
# 평균
avg = sum(num) / n
# 중앙값
middle = sorted(num)

print(round(avg))
print(middle[n//2])

# 최빈값(여러개면 2번째로 작은 값)
many = {}

for i in range(n):
    if num[i] in many:
        many[num[i]] += 1
    else:
        many[num[i]] = 1
m = []
for k, v in many.items():
    if v == max(many.values()):
        m.append(k)
m = sorted(m)
if len(m) == 1:
    print(m[0])
else:
    print(m[1])
# 범위
Min = min(num)
Max = max(num)
print(Max-Min)