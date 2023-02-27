n = int(input())

tower = [int(input()) for _ in range(n)]

stack = []
ans = 0
for i in range(n):
    while stack and tower[stack[-1]] <= tower[i]:
        stack.pop()
        
    stack.append(i)
    ans += len(stack)-1
print(ans)