# 최대공약수의 합

# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

T = int(input())

for t in range(T):
    # 숫자 리스트
    numbers = list(map(int, input().split()))
    
    # 숫자 개수
    num = numbers.pop(0)
    
    # 답
    ans = 0
    
    for i in range(num):
        j = i
        while j < num - 1:
            j += 1
            ans += gcd(numbers[i], numbers[j])

    print(ans)