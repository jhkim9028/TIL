import sys
sys.stdin = open('1859_input.txt')

T = int(input())

for t in range(T):
    n = int(input())
    number = list(map(int,input().split()))
    buy = []
    ans = 0

    if number[0] == max(number):
        print(f'#{t+1} 0')
        continue
    
    for num in range(len(number)):
        if number[0] != max(number):
            buy.append(number[0])
            number.pop(0)
        elif number[0] == max(number):
            ans += number[0] * len(buy) - sum(buy)
            buy = []
            number.pop(0)
    print(f'#{t+1} {ans}')