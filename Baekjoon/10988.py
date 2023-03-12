# 길이가 홀수 짝수 나눠서

word = input()
w = len(word)
stack = ''


for i in range(w//2):
    stack += word[-1]
    word = word[0:len(word)-1]


if stack == word[0:len(stack)]:
    print(1)
else:
    print(0)