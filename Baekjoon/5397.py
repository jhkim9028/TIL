T = int(input())

for t in range(T):
    word = input()
    stack = []
    password = []
    a = 0
    for i in range(len(word)):
        if word[i] == '<':
            if password:
                stack.append(password.pop())
            
        elif word[i] == '>':
            if stack:
                password.append(stack.pop())                
        
        elif word[i] == '-':
            if password:
                password.pop()
        
        else:
            password.append(word[i])
            
    if stack:
        while stack:
            password.append(stack.pop())
    
    print(''.join(password))