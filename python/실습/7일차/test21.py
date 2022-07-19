# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

number = int(input())

# cnt = 0
# a = []
# k = 0
# while number != 0:
#     number //= 10
#     cnt += 1
#     for i in a:
#         k = i
#     print(a[])
# ==================================
# print(int(str(number)[::-1]))

result = 0
while number:
    result *= 10
    result += number%10
    number //= 10
    
print(result)
