N,M = map(int, input().split())

num = list(map(int, input().split()))

for _ in range(M):
    a,b = map(int, input().split())
    
    print(sum(num[a-1:b]))