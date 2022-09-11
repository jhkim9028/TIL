# 한대 1070
# 10대 1700
# 1대 70

# A : 고정비용, B : 한대 비용 C : 노트북 가격

A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(int(A//(C-B)+1))