# i번쨰가 '('이면 스택에 추가
# i번째가 '('가 아니면 경우가 2가지
# i-1번째가 '(' 인 경우 / i-1번쨰가 ')'인 경우
# 앞의 경우가 오면 스택에서 팝하고 스택에 들어있는 개수만큼 답에 더해준다.
# 뒤의 경우가 오면 스택에서 팝하고 1만큼 더해준다. 
n = input()

stack = []
ans = 0

for i in range(len(n)):
    if n[i] == '(':
        stack.append('(')
    else:
        if n[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
            
print(ans)