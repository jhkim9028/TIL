# 킹 1, 퀸 1, 룩 2, 비숍 2, 나이트 2, 폰 8

chess = {
    'king' : 1,
    'queen' : 1,
    'rook' : 2,
    'bishop' : 2,
    'night' : 2,
    'pown' : 8
    }
cnt = []
input_ = list(map(int, input().split()))
for v in chess.values():
    cnt.append(v)

for i in range(len(cnt)):
    print(cnt[i] - input_[i],end=' ')