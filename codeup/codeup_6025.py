#정수 2개를 입력받아
#합을 출력하는 프로그램을 작성해보자.

a,b = input().split()
# input은 모두 string으로 저장됩니다. 아무리 숫자 형태하고 해도요
# 숫자로 활용하기 위해서는 항상 int로 변환!
c = int(a)+int(b)
print(c)