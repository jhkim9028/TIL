import sys
input = sys.stdin.readline

x = int(input())
# 9
# copy가 a-1번째까지 갯수합
# ans가 a번쨰까지 갯수합
# 나는 x번쨰를 구해야 하고
# a가 짝수일 때 홀수일 때 나눠서
a = 0
ans = 0
while True:
    copy = ans
    a += 1
    ans += a

    if copy <= x <= ans:
        break

num = x - copy

up = []
down = []
if not a % 2:
    # 짝수일 때 분자
    for i in range(1,a+1):
        up.append(i)
    
    # 분모
    for j in range(a,0,-1):
        down.append(j)

else:
    # 홀수일 떄 분자
    for k in range(a,0,-1):
        up.append(k)
    
    for l in range(1,a+1):
        down.append(l)

print(up[num-1],'/',down[num-1],sep='')












# up = []
# down = []
# for i in range(1,a+1):
#     # 짝수이면
#     if i % 2:
#         for m in range(i,0,-1):
#             up.append(m)
#         for j in range(1,i+1):
#             down.append(j)
#         # 홀수이면
#     if not i % 2:
#         for k in range(1,i+1):
#             up.append(k)
#         for n in range(i,0,-1):
#             down.append(n)

# print(up[x-1],'/',down[x-1],sep='')