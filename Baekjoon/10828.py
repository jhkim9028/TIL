import sys
input = sys.stdin.readline

N = int(input())

stack = []
for i in range(N):
    word = input().split()
    
    if word[0] == 'push':
        stack.append(word[1])
    elif word[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])