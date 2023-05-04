import sys
input = sys.stdin.readline



while True:
    stack = []
    sen = input().rstrip()
    if sen == '.':
        break
    
    for s in sen:
        if s == '(' or s == '[':
            stack.append(s)
        
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
        
    if len(stack) == 0:
        print('yes')
    else:
        print('no')