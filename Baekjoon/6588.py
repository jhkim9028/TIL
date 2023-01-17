# 6588

# 에라토스테네스의 체 사용

p = 10 ** 6 # 문제에서 범위가 백만까지

prime = [False, False] + [True] * (p-1) # 0,1은 소수가 아니므로 False 나머지는 일단 모두 소수라는 가정하에 시작 p-1은 백만일까지 해야 for문에서 백만까지 되니까

# 에러토스테네스의 체
for i in range(1, int(p ** 0.5) + 1): # 제곱근까지
    if prime[i]: # i번째가 소수라면
        for j in range(2*i, p+1,i): # 2 * i부터 i씩 증가하는데 p+1까지
            prime[j] = False

while True:
    n = int(input())
    if not n:
        break
    else:
        for i in range(1, n+1):
            if prime[i] and prime[n-i]:
                print(f'{n} = {i} + {n-i}')
                break