
# 재귀


N, M = map(int, input().split())
# 1 <= M <= N <= 8
ans = []
# ans에 들어가면 True로 바꿔서 판별
a = [False] * (N + 1)

def NM():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(1, N + 1):
        # True이면 건너뛰어서 중복안되게
        if a[i]:
            continue
        # ans에 넣고 True로 바꾸기
        ans.append(i)
        a[i] = True
        # 재귀
        NM()
        # ans에 넣은 후에 빼고 False로 바꾸기
        ans.pop()
        a[i] = False

NM()