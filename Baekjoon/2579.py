# # # 관점
# # # 내가 올라갈 계단을 생각x
# # # 내가 꼭대기에 있다고 생각하고 밟고 올라온 계단 무엇인지 생각해보자
# # # 내가 n-1계단을 밟은 경우 연속 세 계단은 안되므로 무조건 n-3번째에서 올라온 경우이다
# # # 내가 n-2계단을 밟은 경우와 비교해서 더 큰 경우를 선택해서 더하면 된다.
# # # 3번 째 계단은 밟을 일이 없네?

# n = int(input())

# stair = [int(input()) for _ in range(n)]
# dp = [0] * n

# if n <= 2:
#     print(sum(stair))
# else:
#     dp[0] = stair[0]
#     dp[1] = stair[0]+stair[1]
    
#     for i in range(2,n):
#         dp[i] = max(stair[i]+stair[i-1]+dp[i-3],stair[i]+dp[i-2])
# print(dp[-1])

n=int(input()) # 계단 개수
s=[int(input()) for _ in range(n)] # 계단 리스트
dp=[0]*(n) # dp 리스트
if len(s)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(s))
else: # 계단이 3개 이상일 때
    dp[0]=s[0] # 첫째 계단 수동 계산
    dp[1]=s[0]+s[1] # 둘째 계단까지 수동 계산
    for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])