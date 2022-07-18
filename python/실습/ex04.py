# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.


# words = list(map(int, input().split()))
# print(words)

words = list(map(str, input().split()))
print(words)

# 문자열을 입혁해야하기 때문에 int가 아니라 str이어야 한다.