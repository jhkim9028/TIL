# 17427

# fA = A의 모든 약수의 합
# x보다 작거나 같은 자연수 y의 fY를 더한 값은 gX

n = int(input())
sum = 0

for i in range(1, n+1):
    sum += (n // i) * i
print(sum)