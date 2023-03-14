N = int(input())

star = '*'

space = ' '
stack = []

for i in range(N):
    ans = space*(N-i-1)+star
    print(ans)
    stack.append(ans)
    star += '**'
stack.pop()
for i in range(N-1):
    print(stack.pop())