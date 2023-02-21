n,m = map(int, input().split())

b = [0] * n

for i in range(m):
    q,w,e = map(int, input().split())
    for j in range(q-1,w):
        b[j] = e
    
print(*b)