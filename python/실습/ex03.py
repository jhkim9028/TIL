# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# numbers = input().split()
# print(sum(numbers))
# ============================

numbers = map(int, input().split())
print(sum(numbers))

# 원인은 numbers가 int가 아니라 str이기 때문에 int로 변환하여 sum을 한다.