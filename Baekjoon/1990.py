# # 소수이면서 팰린드롬인 수

#########################################################

# a, b = map(int, input().split())

# # 문제에선 10 ** 9 까지인데 팰린드롬은 10 ** 7 이상에선 없다
# if b > 10 ** 7:
#     b = 10 ** 7

# # 에라토스테네스 체
# che = [False, False] + [True] * (b - 1)

# for i in range(2, b-1):
#     if che[i]:
#         if str(i)[::-1] == str(i) and a <= i:
#             print(i)
#         for j in range(2*i, b+1, i):
#             che[j] = False

# print(-1)

###########################################################

# a, b = map(int, input().split())

# # 문제에선 10 ** 9 까지인데 팰린드롬은 10 ** 7 이상에선 없다
# # 자릿수가 짝수인 팰린드롬은 11밖에 없다
# if b >= 10 ** 7:
#     b = 10 ** 7
# if 10 ** 6 >= b >= 10 ** 5:
#     b = 10 ** 5
# if 10 ** 5 >= b >= 10 ** 4:
#     b = 10 ** 4

# # 에라토스테네스 체
# che = [False] + [True] * (b // 2)

# for i in range(1, len(che)):
#     if che[i]:
#         if str(i*2+1)[::-1] == str(i*2+1) and i*2 + 1 >= a:
#             print(2*i+1)
#         for j in range(i+(2*i+1), len(che), 2*i+1):
#             che[j] = False

# print(-1)



def reverse(text):
    result = ''
    for t in text:
        result = t + result
    return result


n, m = map(int, input().split())
if m >= 10000000:
    m = 10000000
if 1000000 >= m >= 100000:
    m = 100000
if 10000 >= m >= 1000:
    m = 1000

primes = [False] + [True] * (m//2)
for i in range(1, len(primes)):
    if primes[i]:
        if i*2 + 1 >= n and str(i*2+1) == reverse(str(i*2+1)):
            print(2*i+1)
        for j in range(i + (2*i+1), len(primes), 2*i+1):
            primes[j] = False
print(-1)