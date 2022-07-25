# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

import sys

sys.stdin = open("2908_input.txt", "r")

num1, num2 = map(int, input().split())

# 10으로 나눈 나머지를 더하고 거기에 10을 곱하고 다시 나머지를 더하고 10을 곱한다. 반복
rev1 = 0
rev2 = 0
a = 0
b = 0

while True:
    if num1 < 10:
            rev1 += num1
            break
    else:
        a = num1 % 10
        num1 //= 10
        rev1 += a
        rev1 *= 10
        
while True:
    if num2 < 10:
            rev2 += num2
            break
    else:
        b = num2 % 10
        num2 //= 10
        rev2 += b
        rev2 *= 10
if rev1 > rev2:
    print(rev1)
else:
    print(rev2)
# print(rev1) if rev1 > rel2 else print(rev2)
#print(rev1 if rev1 > rev2 else rev2)
#3항연산자 적용