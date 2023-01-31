# N번쨰 손님이 배정받는 방호수
# 호텔의 층수, 각 층의 방 수, 몇 번째 손님인지
T = int(input())


for t in range(T):
    H,W,N = map(int, input().split())
    
    a = [[0 for _ in range(W)]for _ in range(H)]
    
    n = 0
    
    for i in range(W):
        for j in range(H):
            if not a[j][i]:
                a[j][i] = 1
                n += 1
                if n == N:
                    print((j+1) * 100 +(i+1))