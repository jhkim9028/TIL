import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    stack = []
    stack2 = []
    parenthesis = input()
    parenthesis = parenthesis.replace('()','')

    for p in parenthesis:
        if p == '(':
            stack.append(p)
        if p == ')':
            if stack:
                stack.pop()
            else:
                stack2.append(p)
        

    if not stack and not stack2:
        print('YES')
    else:
        print('NO')