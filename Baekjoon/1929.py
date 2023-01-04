# 1929

# decimal : 소수

# M ~ N 사이 소수를 모두 출력
# 소수가 아닌걸 구해서 총 개수 - 소수 아닌 수
# 약수가 2개인 수 구하기(for x for) : 시간 초과
# 2,3,5,7로 나눠지는거 뺴기(for) : 출력 초과


# 에라토스테네스의 체 
import math

M, N = map(int, input().split())
array = [True for i in range(N+1)] # 모든 수가 소수인것으로 초기화

for i in range(2, int(math.sqrt(N))+1): # 2부터 N의 제곱근까지의 모든 수를 확인
    if array[i] == True: # i가 소수인 경우 i를 제외한 i의 모든 배수 지우기
        j = 2
        while i * j <= N:
            array[i*j] = False
            j += 1
# 소수 출력
for i in range(M, N+1):
    if i == 1:
        continue
    if array[i]:
        print(i)