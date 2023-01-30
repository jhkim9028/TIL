# 1713

# 사진틀 개수 (1 <= N <= 20)
# 전체 학생의 총 추천 횟수 (1000이하)
# 추천받은 학생을 나타내는 번호(순서대로)

# 1. 비어있는 사진틀이 없으면, 가장 적은 추천을 받은 학생과 교체
# 2. 가장 적은 추천을 2명 이상 받았으면 더 오래된 사진을 삭제
# 3. 같은 학생이 각각 다른 학생에게 추천 받으면 추천 수 + 1
# 4. 사진틀에서 삭제되면 추천수 리셋

# 비어있는 최종 후보 틀
final = []
# 개수 세기
cnt = {}

# 최종 사진틀 개수
N = int(input())

# 추천 횟수
R = int(input())

# 추천받은 학생 번호
P = list(map(int, input().split()))

for i in range(R):
    # 개수에 있으면 +1하고 넘어가기
    if P[i] in cnt:
        cnt[P[i]] += 1
        continue
    # N개 이하면 사진틀에 추가
    if len(final) < N:
        final.append(P[i])
    # N개면 최소값 구해서 삭제하고 새 값 추가
    # 최소값이 여러개면 가장 오래된 후보 제거 후 추가
    elif len(final) == N:
        a = ''
        for k, v in cnt.items():
          if v == min(cnt.values()):
              a = k
              break
        final.remove(a)
        cnt.pop(a)
        final.append(P[i])
    # 새로 추가한 값 개수에 추가
    if P[i] not in cnt:
        cnt[P[i]] = 1
print(*sorted(final))