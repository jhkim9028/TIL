n = input()

a = 1
ans = 0
stack = []

for i in range(len(n)):
    if n[i] == '(':
        stack.append('(')
        a *= 2
    elif n[i] == '[':
        stack.append('[')
        a *= 3
    elif n[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if n[i-1] == '(':
            ans += a
        stack.pop()
        a //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if n[i-1] == '[':
            ans += a
        stack.pop()
        a //= 3
if stack:
    print(0)
else:
    print(ans)