# A : 올라가는 거리
# B : 미끄러지는 거리
# V : 총 거리
#  (1 <= B < A <= V <= 1,000,000,000)
# 미끄러지는 거리는 최소 1 이상
# 올라가는 거리는  총 거리보다 작거나 같다


A, B, V = map(int, input().split())

# A - B : 올라가는 거리 - 미끄러지는 거리
# V - A : 마지막날 올라가는 거리 뺀 값

#  V - A 에서 A - B를 나눈 몫은 마지막 날 올라가는 걸 뺀 기어오른 날
# 근데 이건 V - A 가 A - B보다 큰 경우
# V - A가 A - B보다 작은 경우 

a = A - B
b = V - B

if b / a > b // a:
    print((b // a )+ 1)
else:
    print(b // a)