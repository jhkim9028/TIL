# 규칙 : 1번 쨰 줄 = 1
# 2번 째 줄 : 6개 (7-2+1)
# 3번 째 줄 : 12개(19 - 8 + 1) 그다음 줄 18개 ... 6의 배수로 늘어남

room = int(input())
a = 1

cnt = 0
while True:
    a += 6 * cnt
    if a < room:
        cnt += 1
    else:
        print(cnt + 1)
        break
