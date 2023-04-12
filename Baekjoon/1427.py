import sys
input = sys.stdin.readline

number = input()

stack = []
arr = []

for i in range(len(number)):
    if not stack:
        stack.append(number[i])
    else:
        if number[i] <= stack[-1]:
            stack.append(number[i])
            continue
        else:
            while True:
                if  not stack or stack[-1] > number[i]:
                    stack.append(number[i])
                    while arr:
                        stack.append(arr.pop())
                    break
                arr.append(stack.pop())

print(''.join(stack))