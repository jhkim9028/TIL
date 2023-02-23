n, m = map(int, input().split())
ball = []

for i in range(1,n+1):
    ball.append(i)

for i in range(m):
    stack = []
    a,b = map(int,input().split())
    stack.append(ball[a-1])
    ball[a-1] = ball[b-1]
    ball[b-1] = stack[0]

print(*ball)