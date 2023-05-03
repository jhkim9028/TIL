import sys
input = sys.stdin.readline

T = int(input())

stack = []
for t in range(T):
    num = int(input())
    if t != 0 and not num:
        stack.pop()
    
    else:
        stack.append(num)

print(sum(stack))