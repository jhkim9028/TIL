# 단어를 입력받는다
# 공백과 '<'가 기준이 된다
# 1. 공백 기준으로 단어나누기
# 2. 꺽새 기준으로 뒤집지 않기
# 기준으로 2파트로 나눠서 따로 코드 짜고 합침

S = str(input())
a = True # 뒤집기 기준
stack = []
ans = ''

for i in range(len(S)):
    # 뒤집지 않는 기준
    if S[i] == '<':
        # 스택에 무언가 들어있으면
        if len(stack) != 0:
            while True:
                ans += stack.pop()
                if not len(stack):
                    break
        ans += S[i]
        a = False
        continue
    if S[i] == '>':
        ans += S[i]
        a = True
        continue
    # 뒤집지 않는다
    if not a:
        ans += S[i]
    # 뒤집는다
    if a:
        # 공백 기준 단어 나누기
        if S[i] == ' ':
            while True:
                ans += stack.pop()
                if not len(stack):
                    ans += ' '
                    break
        # 공백이 아니라면
        else:
            stack.append(S[i])
        # 마지막 단어는 공백이 없으므로
        if i == len(S)-1:
            while True:
                ans += stack.pop()
                if not len(stack):
                    ans += ' '
                    break
    # '>'이후에 나오는 단어가 있는 경우
    if i == len(S)-1 and len(stack) >= 1:
        while len(stack) != 0:
            ans += (stack.pop(0))

        
print(ans)

